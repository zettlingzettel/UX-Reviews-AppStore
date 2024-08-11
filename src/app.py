from flask_sqlalchemy import SQLAlchemy
import json
import pandas as pd
import numpy as np
import json
from flask import jsonify

from flask import Flask, render_template, request, current_app
import sqlite3
import requests
import spacy
import pytextrank
import time
import git
# from git import Repo

nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)


@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./UX-Reviews-AppStore')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200


app_health = {"Health": ""}
database_name = f"AppReviews.db"
db_results = []
app.start_time = time.time()
app_metrics = {"requests": 0, "response_time": 0, "requests_per_second": 0}

def update_metrics(response_time):
    app_metrics["requests"] += 1
    app_metrics["response_time"] += response_time
    total_time = time.time() - app.start_time
    app_metrics["requests_per_second"] = app_metrics["requests"] / total_time



def save_to_database(data, table_name):
    table_name = "AppReviews"
    try:
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()

        cursor.execute(f'''
                   CREATE TABLE IF NOT EXISTS {table_name} (
                       id INTEGER PRIMARY KEY,
                       data TEXT NOT NULL
                   )
               ''')


        serialized_dict = str(data)
        cursor.execute(f'''
            INSERT INTO {table_name} (data)
            VALUES (?)
        ''', (serialized_dict,))

        connection.commit()
        connection.close()


    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

def app_health_checker(database):
    try:
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT 1')
            db_check = cursor.fetchone()
            if db_check[0] is not None:
                return f"Database is not empty", 200
            else:
                f"Database is empty, Error: {str(e)}", 500
    except Exception as e:
        return f"App is not healthy, Error: {str(e)}", 500

@app.route('/', methods=['GET', 'POST'])
def index():
    page = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>App Store Review Search</title>
    </head>
    <body>
        <h1>Search for App Store Apps 1</h1>
        <form action="/search" method="POST">
            <p>What's app id?</p>
            <p>Examples: Genshin Impact - 1517783697; Obsidian - 1557175442; Formula 1 app - 835022598</p>
            <p>You can find App Store app id in app's url (e.g. https://apps.apple.com/us/app/formula-1/id<b><u>835022598</u></b>)</p> 
            <input name="appid" id="appid" type="text" /><br>
            <input type="submit" value="Search""/>
        </form>
    </body>
    </html>
    """
    return (page)

@app.route('/search', methods=['POST', 'GET'])


def get_app_id():
    global app_id
    app_id = request.form.get("appid", "")
    return api_call()

def api_call():
    global data
    global reviews
    global reviews_text
    reviews_text = []
    reviews = []

    global response

    url_address = "https://itunes.apple.com/us/rss/customerreviews/page=1/id=" + str(
        app_id) + "/sortBy=mostRecent/json"

    response = requests.get(url_address)

    if response.status_code == 200:
        data = response.json()
        reviews = data.get("reviews", [])
        reviews.append(data)
        reviews = reviews[0]["feed"]["entry"]
        search()
        return search()
    else:
        print("Error: ", response.status_code)

def search():
    global result
    checkpoint_start_time = time.time()
    update_metrics(time.time() - checkpoint_start_time)

    for i in range(len(reviews)):
        review = reviews[i]
        username = review["author"]["name"]["label"]
        content = review["content"]["label"]
        reviews_text.append({"username": username, "content": content})
        save_to_database(reviews, "AppReviews")
        db_results.append(reviews)

        app_health["Health"] = app_health_checker(database_name)
        analysed_data = analysis(reviews)
        return analysed_data




def analysis(reviews):
    global analyzed_texts
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank")

    analyzed_texts = []
    for i in range(len(reviews)):
        review = reviews[i]
        review_str = review["content"]["label"]
        doc = nlp(review_str)
        key_phrases = [phrase.text for phrase in doc._.phrases[:10]]
        analyzed_texts.append({"review": review_str, "keywords": key_phrases})

        html_analyzed_data = f"""
        """
        for i in range(len(analyzed_texts)):
            analyzed_text = analyzed_texts[i]
            analyzed_text_str = analyzed_text["review"]
            analyzed_text_keywords = analyzed_text["keywords"]
            analyzed_text_str_total = f"""
            Review: {analyzed_text_str}, <br>
            Keywords: {analyzed_text_keywords}<br><br>
            """

            html_analyzed_data += analyzed_text_str_total

        html_analyzed = f"""
               <!DOCTYPE html>
               <html>
               <head>
                   <title>Reviews</title>
               </head>
               <body>
                   <h1>Reviews Analyzed</h1>
                   {html_analyzed_data}
               </body>
               </html>
               """
    # return analyzed_texts
    return html_analyzed








@app.route('/database_data')
def database_data():
    return db_results
@app.route('/health')
def health_check_function():
    return app_health

@app.route('/metrics')
def define_metrics():
    metrics= {
        "requests": app_metrics["requests"],
        "response_time": app_metrics["response_time"],
        "requests_per_second": app_metrics
    }
    return metrics


if __name__ == "__main__":
    app.run(debug=False)




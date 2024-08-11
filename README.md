<u>What does this application do? </u>
- scrapes the reviews from the AppStore
- saves it into the database
- performs a text analysis identifying the keywords in each review

<u>Instructions for running the application:</u>
Deactivate .venv if it is running with
```deactivate```

Activate venv with
```source venv/bin/activate```

Export the app with
```export FLASK_APP=src/app.py```

Run the app with
```flask run```

The server is running locally on http://127.0.0.1:5000

App id includes only digits (without letters or spaces)


Please access the following endpoints after submitting the form:
* Application health endpoint: http://127.0.0.1:5000/health

* Application metrics endpoint: http://127.0.0.1:5000/metrics

* Application Database Results endpoint: http://127.0.0.1:5000/database_data

To run unit tests go to the `/src/tests` folder and run
```python -m test_all_unit_tests```

To run integration tests go to the `/src/tests` folder and run
```python -m test_all_integration_tests```


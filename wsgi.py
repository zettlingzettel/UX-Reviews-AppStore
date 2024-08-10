
import sys
# current_path = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.join(current_path, "lib"))
#
# from app import app as application

# path = '/home/antinomy/testenv'
# if path not in sys.path:
#     sys.path.append(path)
#

# from quick_session import app as application



project_home = '/home/sillybilly777/UX-Reviews-AppStore/src'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from my_flask_app import app as application

# from src import app
#
# if __name__ == "__main__":
#     app.run()


# project_home = u'/home/DrAgus/mysite'
# path = 'my_flask_app/src/app'
# if path not in sys.path:
#    sys.path.insert(0, path)
#
# from app import app as application
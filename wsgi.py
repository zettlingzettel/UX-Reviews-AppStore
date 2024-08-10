
import sys

project_home = '/home/sillybilly777/UX-Reviews-AppStore/src'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application

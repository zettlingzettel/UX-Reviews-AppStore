import sys

# add your project directory to the sys.path
project_home = '/home/sillybilly777/UX-Reviews-AppStore'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from src.app import app as application
# application = create_app()

# # import sys

# # project_home = '/home/sillybilly777/UX-Reviews-AppStore'
# # if project_home not in sys.path:
# #     sys.path.insert(0, project_home)

# # from app import app as application

# import sys
# #
# ## The "/home/alinecatikoc" below specifies your home
# ## directory -- the rest should be the directory you uploaded your Flask
# ## code to underneath the home directory.  So if you just ran
# ## "git clone git@github.com/myusername/myproject.git"
# ## ...or uploaded files to the directory "myproject", then you should
# ## specify "/home/alinecatikoc/myproject"



# path = "/home/sillybilly777/UX-Reviews-AppStore"
# if path not in sys.path:
#     sys.path.append(path)

# from .src import app as application
# # path = '/home/sillybilly777/UX-Reviews-AppStore'
# # if path not in sys.path:
# #   sys.path.insert(path)

# # from app import app as application
# # try:
# #     from app import app as application
# #     print("Import successful!")
# # except ImportError as e:
# #     print(f"Import failed: {e}")

# # import os
# # from dotenv import load_dotenv
# # project_folder = os.path.expanduser(path)  # adjust as appropriate
# # load_dotenv(os.path.join(project_folder, '.env'))

# # from app import app as application
# # from flaskai import app as application

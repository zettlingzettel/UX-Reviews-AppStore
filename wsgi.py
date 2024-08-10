import sys
import os
# path = './src'
# if path not in sys.path:
#    sys.path.insert(0, path)

# sys.path.insert(0,
# os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir), "lib"))
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, "lib"))

from app import app as application
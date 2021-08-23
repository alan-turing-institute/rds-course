import logging
import os
import sys
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.insert(0, root_path)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
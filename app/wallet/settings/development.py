import os
from dotenv import load_dotenv

APP_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../'))
dotenv_path = os.path.join(APP_DIR, 'env', '.development')
load_dotenv(dotenv_path)

from .base import * #noqa

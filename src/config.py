import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('TOKEN', '')
DB_NAME = os.environ.get('DB_NAME', '')
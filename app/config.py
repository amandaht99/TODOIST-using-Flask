from os import environ
from dotenv import load_dotenv

TOPICS_PER_PAGE = 15
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

load_dotenv()
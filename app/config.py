from os import environ
from dotenv import load_dotenv


TOPICS_PER_PAGE = 5
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
SECRET_KEY = environ.get('SECRET_KEY')

load_dotenv()


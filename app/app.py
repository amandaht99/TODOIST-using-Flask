from . import cookies
from flask import Flask, redirect, url_for, render_template
from app.extensions.database import db, migrate
from app.extensions.authentication import login_manager
from os import environ


""" Creates a Flask app instance """
def create_app():
  app = Flask(__name__)
  app.secret_key = environ.get('SECRET_KEY')
  app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DATABASE_URL')

  register_extensions(app)
  register_blueprints(app)
  return app

""" Registers cookies blueprint """
def register_blueprints(app: Flask):
  app.register_blueprint(cookies.routes.blueprint)

""" Registers extensions for Flask app """
def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db, compare_type=True)
  login_manager.init_app(app)
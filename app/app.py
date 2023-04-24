from . import cookies
from flask import Flask, redirect, url_for, render_template
from app.extensions.database import db, migrate
from app.extensions.authentication import login_manager

def create_app():
  app = Flask(__name__)
  # app.config.from_object('app.config')
  app.secret_key = "HsfQThoXlTn9F3Y3UGTkkZEnLY5vpZ2a"
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

  register_extensions(app)
  register_blueprints(app)
  return app

def register_blueprints(app: Flask):
  app.register_blueprint(cookies.routes.blueprint)

def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db, compare_type=True)
  login_manager.init_app(app)
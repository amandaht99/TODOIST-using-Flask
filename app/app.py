from . import cookies
from flask import Flask, redirect, url_for, render_template
from extensions.database import db, migrate

def register_blueprints(app: Flask):
  app.register_blueprint(cookies.routes.blueprint)

print("dings")


def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')

  print("inside create_app")

  register_extensions(app)
  register_blueprints(app)
  return app

def register_extensions(app: Flask):
  print("trying to initialiize app")

  print(db)
  db.init_app(app)
  migrate.init_app(app, db, compare_type=True)
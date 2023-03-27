from database.extensions.database import db

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  slug = db.Column(db.String(80), unique=True)
  name = db.Column(db.String(80))
  description = db.Column(db.String(150))

"""class Cookie():
  id = ''
  slug = ''
  name = ''
  price = ''"""


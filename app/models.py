from app.extensions.database import db

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  name = db.Column(db.String(80))
  description = db.Column(db.String(150))
  topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Topic(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  slug = db.Column(db.String(80), unique=True)
  name = db.Column(db.String(20))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  todos = db.relationship('Todo', backref='topic', lazy=True)
  
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  username = db.Column(db.String(15), unique=True)
  email = db.Column(db.String(50), unique=True)
  password = db.Column(db.String)



"""class Cookie():
  id = ''
  slug = ''
  name = ''
  price = ''"""


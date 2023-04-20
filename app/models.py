from app.extensions.database import db, CRUDMixin

class Topic(db.Model, CRUDMixin):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  name = db.Column(db.String(20))
  description = db.Column(db.String(1024))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
class User(db.Model, CRUDMixin):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  username = db.Column(db.String(15), unique=True)
  email = db.Column(db.String(50), unique=True)
  password = db.Column(db.String)
  topics = db.relationship('Topic', backref='topic', lazy=True)


"""class Cookie():
  id = ''
  slug = ''
  name = ''
  price = ''"""


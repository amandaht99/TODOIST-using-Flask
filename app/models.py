from app.extensions.database import db, CRUDMixin

class Topic(db.Model, CRUDMixin):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  slug = db.Column(db.String(80), unique=True)
  name = db.Column(db.String(20))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
class User(db.Model, CRUDMixin):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  username = db.Column(db.String(15), unique=True)
  email = db.Column(db.String(50), unique=True)
  password = db.Column(db.String)



"""class Cookie():
  id = ''
  slug = ''
  name = ''
  price = ''"""


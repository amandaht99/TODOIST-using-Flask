from flask_login import LoginManager
from app.models import User

login_manager = LoginManager()

""" Load user by user ID """
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
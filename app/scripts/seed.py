from app.app import create_app
from app.models import Topic, User
from app.extensions.database import db


""" Runs the Flask application """
if __name__ == '__main__':
  app = create_app()
  app.app_context().push()

"""  Instances of Topic model """
topic_data = {
    'shopping': {'name': 'Shopping' },
    'work': {'name': 'Work'},
    'today': {'name': 'Today'},
}

""" Instances of User Model """
user_data = {
    'maxmusterman': {'username': 'Maxmusterman', 'email': 'maxmusterman@gmail.com', 'password': '12345'},
    'ashley': {'username': 'Ashley', 'email': 'ashleyburnout@gmail.com', 'password': '1234'},
    'toby': {'username': 'Toby45', 'email': 'toby45@gmail.com', 'password': 'password'},
}

""" Add instances to session """
for slug, topic in topic_data.items():
  new_topic = Topic(slug=slug, name=topic['name'])
  db.session.add(new_topic)

""" Commit changes to database """
db.session.commit()
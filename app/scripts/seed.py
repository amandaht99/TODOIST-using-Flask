from app.app import create_app
from app.models import Topic, User
from app.extensions.database import db

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()


topic_data = {
    'shopping': {'name': 'Shopping' },
    'work': {'name': 'Work'},
    'today': {'name': 'Today'},
}

user_data = {
    'maxmusterman': {'username': 'Maxmusterman', 'email': 'maxmusterman@gmail.com', 'password': '12345'},
    'ashley': {'username': 'Ashley', 'email': 'ashleyburnout@gmail.com', 'password': '1234'},
    'toby': {'username': 'Toby45', 'email': 'toby45@gmail.com', 'password': 'password'},
}

for slug, topic in topic_data.items():
  new_topic = Topic(slug=slug, name=topic['name'])
  db.session.add(new_topic)

db.session.commit()

'''for slug, user in user_data.items():
  new_user = User(username=user['username'], email=user['email'], password=user['password'])
  db.session.add(new_user)

db.session.commit()'''
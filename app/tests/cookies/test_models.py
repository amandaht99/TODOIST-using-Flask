from app.extensions.database import db
from app.models import Topic

def test_topic_update(client):
  # updates cookie's properties
  topic = Topic(name='Shopping')
  db.session.add(topic)
  db.session.commit()

  topic.name = 'School'
  topic.save()

  updated_topic = Topic.query.filter_by(slug='shopping').first()
  assert updated_topic.name == 'Shopping'

def test_topic_delete(client):
   #deletes topic
   topic = Topic(name='House')
   db.session.add(topic)
   db.session.commit()

   topic.delete()

   deleted_topic = Topic.query.filter_by(slug='house').first()
   assert deleted_topic is None

def test_web_up(client):
    response = client.get('/')
    assert response.status_code == 200
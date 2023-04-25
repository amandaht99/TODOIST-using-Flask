from app.models import Topic, User


#Test renders newlists on GET.
""" def test_get_newlist_renders(client):
  # Page loads and renders newlists
  response = client.get('/newlist')
  assert b'new list' in response.data """

# Creates an order record
def test_post_newlist_creates_topic(client):
    response = client.post('/newlist', data={
        'name': 'coding'
    })
    assert Topic.query.first() is not None

#Test creates todo on POST.
""" def test_post_newlist_creates_todo(client):
  # Creates an todo related to the topic
  response = client.post('/newlist', data={
    'name': 'dishes',
    'description': 'wash the dishes'
  })
  assert Todo.query.first() is not None """


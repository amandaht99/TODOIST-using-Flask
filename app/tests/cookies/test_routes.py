from app.models import Topic


# Page loads and renders cookies
def test_topics_renders_topics(client):
    new_topic = Topic(name='Shopping')
    new_topic.save()

    response = client.get('/lists')

    assert b'Shopping' in response.data
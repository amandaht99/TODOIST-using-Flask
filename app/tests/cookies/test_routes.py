from app.models import Topic

def test_topics_renders_topics(client):
    # Page loads and renders cookies
    new_topic = Topic(name='Shopping')
    new_topic.save()

    response = client.get('/lists')

    assert b'Shopping' in response.data
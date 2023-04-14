from flask import Blueprint, render_template, redirect, request, current_app
from app.models import Topic, User
from app.config import TOPICS_PER_PAGE

list_data = {
    'shopping': {'name': 'Shopping List', 'item': 'tomatos'},
    'work': {'name': 'Work To-Dos', 'item': ['attend meeting at 12', 'practice active listening']},
    'today': {'name': 'Today', 'item': 'vacuum the house'},
}

blueprint = Blueprint('cookies', __name__)

@blueprint.route('/')
def index():
  return render_template('index.html')

@blueprint.route('/index.html')
def index_redirect():
  return redirect('/')

@blueprint.route('/lists')
def topics():
    page_number = request.args.get('page', 1, type=int)
    #all_topics = Topic.query.all()
    topics_pagination = Topic.query.paginate(page= page_number, per_page=TOPICS_PER_PAGE)
    return render_template('lists.html', topics_pagination=topics_pagination)

@blueprint.route('/lists.html')
def lists_redirect():
   return redirect('/lists')

@blueprint.route('/lists/<id>')
def topic(id):
    topic = Topic.query.filter_by(id=id).first_or_404()
    listname = topic.name

    listdesc = topic.description.split('\n')
    return render_template('list_items.html', listname=listname, listdesc=listdesc)

@blueprint.route('/lists/<id>/edit')
def editlist(id):
  topic = Topic.query.filter_by(id=id).first_or_404()
  listname = topic.name

  listdesc = topic.description.split('\n')
  return render_template('editlistform.html', listname=listname, listdesc=listdesc)
   

@blueprint.route('/newlist', methods=['GET', 'POST'])
def newlist():
  if request.method == "POST":
    topic = Topic(
      name=request.form['list-name'],
      description=request.form['list-items']
    )
    topic.save()
    print(request.form['list-name'])
    print(request.form["list-items"])
  return render_template('newlistform.html')

""" @blueprint.route('/newlist')
def post_newlist():
   # Create a new topic
   todo = Todo(
      name=request.form('name')
   )
   todo.save()


   topics = Topic.query.all()
   return render_template('newlistform.html', topics=topics) """
   

@blueprint.route('/about')
def about():
  return render_template('about.html')

@blueprint.route('/about.html')
def about_redirect():
  return redirect('/about')

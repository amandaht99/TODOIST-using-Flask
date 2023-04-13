from flask import Blueprint, render_template, redirect, request, current_app
from app.models import Todo, Topic, User
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

@blueprint.route('/lists/<slug>')
def topic(slug):
    topic = Topic.query.filter_by(slug=slug).first_or_404()
    return render_template('list_items.html', topic=topic)

@blueprint.route('/newlist', methods=['GET', 'POST'])
def newlist():
  if request.method == "POST":
    print(request.form['list-name'])
    print("amanda")
  return render_template('newlistform.html')

@blueprint.route('/about')
def about():
  return render_template('about.html')

@blueprint.route('/about.html')
def about_redirect():
  return redirect('/about')

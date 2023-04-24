from flask import Blueprint, render_template, redirect, request, current_app, url_for
from app.models import Topic, User
from app.config import TOPICS_PER_PAGE
from app.extensions.database import db
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

list_data = {
    'shopping': {'name': 'Shopping List', 'item': 'tomatos'},
    'work': {'name': 'Work To-Dos', 'item': ['attend meeting at 12', 'practice active listening']},
    'today': {'name': 'Today', 'item': 'vacuum the house'},
}

blueprint = Blueprint('cookies', __name__)

""" Start page """
@blueprint.route('/')
def index():
  return redirect('/login')

""" List Overview """
@blueprint.route('/lists')
@login_required
def topics():
    page_number = request.args.get('page', 1, type=int)
    #all_topics = Topic.query.all()
    topics_pagination = Topic.query.paginate(page= page_number, per_page=TOPICS_PER_PAGE)
    return render_template('lists.html', topics_pagination=topics_pagination)

@blueprint.route('/lists.html')
@login_required
def lists_redirect():
   return redirect('/lists')

""" Specific List """
@blueprint.route('/lists/<id>')
@login_required
def topic(id):
    topic = Topic.query.filter_by(id=id).first_or_404()
    listname = topic.name

    listdesc = topic.description.split('\n')
    return render_template('list_items.html', listname=listname, listdesc=listdesc, id=id)

""" Edit List """
@blueprint.route('/lists/<id>/edit', methods=['GET', 'POST'])
@login_required
def editlist(id):
  topic = Topic.query.filter_by(id=id).first_or_404()
  if request.method == 'POST':
    topic.name = request.form['list-name']
    topic.description = request.form['list-items']
    db.session.commit()
    return redirect(f'/lists/{id}')

  listname = topic.name
  listdesc = topic.description.split('\n')
  return render_template('editlistform.html', listname=listname, listdesc=listdesc, id=id)

""" Delete List """
@blueprint.route('/lists/<id>/delete', methods=['POST']) 
@login_required  
def deletelist(id):
  topic = Topic.query.filter_by(id=id).first_or_404()
  topic.delete()
  return redirect('/lists')

""" Create List """
@blueprint.route('/newlist', methods=['GET', 'POST'])
@login_required
def newlist():
  if request.method == "POST":
    topic = Topic(
      name=request.form['list-name'],
      description=request.form['list-items']
    )
    topic.save()
    return redirect('/lists')
  return render_template('newlistform.html')

""" About Page """
@blueprint.route('/about')
@login_required
def about():
  return render_template('about.html')

@blueprint.route('/about.html')
@login_required
def about_redirect():
  return redirect('/about')



""" Register """
@blueprint.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template('users/register.html')
   
  try:
    if request.form.get('password') != request.form.get('password_confirmation'):
        return render_template('users/register.html', error='The password confirmation must match the password.')
    elif User.query.filter_by(email=request.form.get('email')).first():
        return render_template('users/register.html', error='The email address is already registered.')
    elif User.query.filter_by(email=request.form.get('username')).first():
        return render_template('users/register.html', error='The username is already registered.')
      
    user = User(
          username=request.form.get('username'),
          email=request.form.get('email'),
          password=generate_password_hash(request.form.get('password'))
    )
    user.save()

    login_user(user)
    return redirect('/lists')
  
  except Exception as error_message:
    error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
    return render_template('users/register.html', error=error)

""" Login """
@blueprint.route('/login', methods=['GET', 'POST'])
def login():
  print("login", request.method, request.form, request.form.get("email"))
  if request.method == 'GET':
      return render_template('users/login.html')
  try:
    user = User.query.filter_by(email=request.form.get('email')).first()
    print("user 1", user)

    if not user:
      raise Exception('No user with the given email address was found.')
    elif not check_password_hash(user.password, request.form.get('password')):
      raise Exception('The password does not appear to be correct.')
      
    print('glgkg', login_user, user)
    login_user(user)
    return redirect('/lists')
      
  except Exception as error_message:
    error = error_message or 'An error occurred while logging in. Please verify your email and password.'
    return render_template('users/login.html', error=error)
  
""" Logout """
@blueprint.get('/logout')
def logout():
  logout_user()

  return redirect('/login')
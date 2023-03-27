from flask import Blueprint, render_template, redirect

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
def lists():
    lists_list = ['shopping', 'work', 'today']
    return render_template('lists.html', list=list_data)

@blueprint.route('/lists.html')
def lists_redirect():
  return redirect('/lists')

@blueprint.route('/lists/<slug>')
def list_items(slug):
    if slug not in list_data:
        return "List not found"
    return render_template('list_items.html', list_name=list_data[slug]['name'], items=list_data[slug]['item'])

@blueprint.route('/about')
def about():
    return render_template('about.html')

@blueprint.route('/about.html')
def about_redirect():
  return redirect('/about')

"""
@app.route('/<name>')
def hello_name(name):
    return f'Hello, {name}!'

@app.route('/user/<username>')
def user_profile(username):
  return render_template('user.html', username=username)
"""
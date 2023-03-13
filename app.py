from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

app.config.from_object('config')

list_data = {
    'shopping': {'name': 'Shopping List', 'item': 'tomatos'},
    'work': {'name': 'Work To-Dos', 'item': 'attend meeting at 12'},
    'today': {'name': 'Today', 'item': 'vacuum the house'},
}

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/index.html')
def index_redirect():
  return redirect('/')

@app.route('/lists')
def lists():
    lists_list = ['shopping', 'work', 'today']
    return render_template('lists.html', list=list_data)

@app.route('/lists.html')
def lists_redirect():
  return redirect('/lists')

@app.route('/lists/<slug>')
def list_items(slug):
    if slug not in list_data:
        return "List not found"
    return render_template('list_items.html', list_name=list_data[slug]['name'], items=list_data[slug]['item'])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about.html')
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



#The condition makes sure the server is only started if the app.py file is executed directly and not executed whenever we access the file by, e.g., importing it.
if __name__ == '__main__':
  app.run()
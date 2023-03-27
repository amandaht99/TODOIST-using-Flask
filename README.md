# TODOIST
## Project Description
* TODOIST is a To-Do list for multiple users in the form of a web application

The purpose of TODOIST is to help you organize and prioritize tasks that you need to complete. By creating a list of tasks, you can keep track of what needs to be done, when it needs to be done, and in what order.
Overall, the purpose of TODOIST is to help you stay organized, focused, and productive, while minimizing the risk of forgetting important tasks or falling behind on deadlines.

## Tech Stack
* Click 8.1.3
* Colorama 0.4.6
* Flask 2.2.3
* itsdangerous 2.1.2
* Jinja2 3.1.2
* MarkupSafe 2.1.2
* python-dotenv 1.0.0
* Werkzeug 2.2.3

## MVP Goals
* Users and their tasks are saved in a database
* Authentification for all users (Registration, Login, Log-out)
* Users can only create/view/edit/delete their own tasks
* Users can maybe share a to-do list with another user and collaborate on this 

## Data Models
class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  name = db.Column(db.String(80))
  description = db.Column(db.String(150))
  topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Topic(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  name = db.Column(db.String(20))
  todos = db.relationship('Todo', backref='topic', lazy=True)
  users = db.relationship('User', backref='topic', lazy=True)
  
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  username = db.Column(db.String(15), unique=True)
  email = db.Column(db.String(50), unique=True)
  password = db.Column(db.String)

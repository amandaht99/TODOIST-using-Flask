from app.app import create_app

app = create_app()

#The condition makes sure the server is only started if the app.py file is executed directly and not executed whenever we access the file by, e.g., importing it.
if __name__ == '__main__':
  app.run()
from app.app import create_app

app = create_app()

#Ensures server only started when run directly
if __name__ == '__main__':
  app.run()
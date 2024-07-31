from dotenv import load_dotenv
from app import create_app 

# Load environment variables
load_dotenv()

# Initialize Flask app
app = app = create_app()

if __name__ == '__main__':
  app.run(
    host=app.config.get('HOST', '127.0.0.1'),
    port=app.config.get('PORT', 5000),
    debug=app.config['DEBUG']
  )
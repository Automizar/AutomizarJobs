# config.py

# Flask settings
FLASK_SERVER_NAME = 'localhost:5000'
FLASK_DEBUG = True  # Do not use debug mode in production

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskProjectAutomizar.db'  # Database file
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret key for session management
SECRET_KEY = 'your_random_secret_key'

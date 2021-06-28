import os 

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# sets the project to the app folder
load_dotenv(os.path.join(basedir, '.env'))
#communicates with .env file



class Config():
    """
    Set Config variables for the flask app.
    Using environment variables where available
    Otherwise create the config variable if not done already

    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEPLOY_DATABASE_URL") or 'sqlite:///' or os.path.join(basedir, 'app.db')   
    # add database url to .env file
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Turn off update messages
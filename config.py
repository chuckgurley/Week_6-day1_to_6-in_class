import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
                
#gi
# #)
#from the base

load_dotenv(os.path.join(basedir, '.env'))


class Config():
    """
    set configuration variables for flask app.
    Using environment variables where avalible
    otherwise create the config variable if not done
    already  
    
    """
    FLASK_APP = os.environ.get('FLASK_APP') 
    FLASK_ENV = os.environ.get('FLASK_ENV') 

    SECRET_KEY  = os.environ.get("SECRET_KEY") or "nana nana boo boo youll never guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("database_url") or "sqlite:///" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_MODIFICATIONS = False  #turn of messages from sqlalchemy regaurding updates to our db



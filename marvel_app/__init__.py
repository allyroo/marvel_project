from flask import Flask

app = Flask(__name__)

from .api.routes import api
from .site.routes import site
from .authentication.routes import auth
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from marvel_app.models import db as root_db, login_manager, ma

# Import for Flask-Marshmallow
from flask_marshmallow import Marshmallow

from flask_cors import CORS

from marvel_app.helpers import JSONEncoder




app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)

root_db.init_app(app)

migrate = Migrate(app,root_db)

login_manager.init_app(app)
login_manager.login_view = 'signin' # Specify what page to load for NON-AUTHED users

ma.init_app(app)

app.json_encoder = JSONEncoder

CORS(app)

import marvel_app.models
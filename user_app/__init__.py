from flask import Flask
from .api.routes import api
from .home.routes import home
from .config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


# Initialize database, bcrypt, and JWT
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

# Create the Flask app
def create_app(config_name: str) -> Flask:
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(home)

    app.config.from_object(app_config[config_name])

    # Initialize the extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    return app

app = create_app('development')

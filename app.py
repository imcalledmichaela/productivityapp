from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


"""Construct the core application."""
app = Flask(__name__, instance_relative_config=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:productive@productive.ck04jav5vuqu.us-east-1.rds.amazonaws.com/productive'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db.init_app(app)

with app.app_context():
    CORS(app, resources={r'/*': {'origins': '*'}})
    db.create_all()  # Create sql tables for our data models

from productivityapp.auth import app_auth
app.register_blueprint(app_auth)

from productivityapp.routes import app_routes
app.register_blueprint(app_routes)
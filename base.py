from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.getenv('FLASK_ENV', 'config.DevelopmentConfig'))
db = SQLAlchemy(app)

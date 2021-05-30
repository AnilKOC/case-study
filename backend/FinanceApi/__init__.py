from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:159357@localhost/postgres'
api = Api(app)
db = SQLAlchemy(app)

from . import routes
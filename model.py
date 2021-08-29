from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import datetime 
from marshmallow import Schema, post_dump, post_load , fields
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    time = db.Coloumn(db.DateTime,default = datetime.datetime.now())

    def __init__(self, id, time):
        self.id = id
        self.time = datetime.datetime.now()


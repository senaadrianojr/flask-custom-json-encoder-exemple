from flask import Flask
from flask_pymongo import PyMongo
from configurations.enconder import MongodbJSONEncoder


app = Flask(__name__)
app.config.from_object('config.MyConfig')
app.json_encoder = MongodbJSONEncoder
mongo = PyMongo(app)

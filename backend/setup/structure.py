from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
import datetime, json, pymysql, requests
from flask_marshmallow import Marshmallow
# from flask_cors import CORS


app = Flask(__name__)
# CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()


db = SQLAlchemy(app)
marsh = Marshmallow(app)
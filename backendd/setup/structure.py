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


class Tasks(db.Model):
    __tablename__ = "task"
    task_id = db.Column(db.Integer, primary_key = True)
    task_name = db.Column(db.String(100))
    part_number = db.Column(db.String(100))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, task_name, part_number):
        self.task_name = task_name
        self.part_number = part_number


class Countries(db.Model):
    __tablename__ = "country"
    country_id = db.Column(db.Integer, primary_key = True)
    country_name = db.Column(db.String(100))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, country_name):
        self.country_name = country_name


class Provinces(db.Model):
    __tablename__ = "province"
    province_id = db.Column(db.Integer, primary_key = True)
    province_name = db.Column(db.String(100))
    country_id = db.Column(db.Integer, ForeignKey("country.country_id"))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, province_name, country_id):
        self.province_name = province_name
        self.country_id = country_id


class Plants(db.Model):
    __tablename__ = "plant"
    plant_id = db.Column(db.Integer, primary_key = True)
    plant_name = db.Column(db.String(100))
    province_id = db.Column(db.Integer, ForeignKey("province.province_id"))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, plant_name, province_id):
        self.plant_name = plant_name
        self.province_id = province_id


class Processes(db.Model):
    __tablename__ = "process"
    process_id = db.Column(db.Integer, primary_key = True)
    process_name = db.Column(db.String(100))
    plant_id = db.Column(db.Integer, ForeignKey("plant.plant_id"))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, process_name, plant_id):
        self.process_name = process_name
        self.plant_id = plant_id


class ProcessLines(db.Model):
    __tablename__ = "processline"
    processline_id = db.Column(db.Integer, primary_key = True)
    processline_name = db.Column(db.String(100))
    process_id = db.Column(db.Integer, ForeignKey("process.process_id"))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, processline_name, process_id):
        self.processline_name = processline_name
        self.plant_id = process_id


class AutonomousMobileRobots(db.Model):
    __tablename__ = "autonomousmobilerobot"
    autonomousmobilerobot_id = db.Column(db.Integer, primary_key = True)
    autonomousmobilerobot_name = db.Column(db.String(100))
    processline_id = db.Column(db.Integer, ForeignKey("processline.processline_id"))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, autonomousmobilerobot_name, processline_id):
        self.autonomousmobilerobot_name = autonomousmobilerobot_name
        self.plant_id = processline_id
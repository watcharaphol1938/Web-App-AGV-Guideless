from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
import datetime
from flask_marshmallow import Marshmallow
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/amrdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)
marsh = Marshmallow(app)


# Structure -------------------------------------------------------------------------------------------
# Country --------------------------------------------------------------
class Countries(db.Model):
    __tablename__ = "country"
    country_id = db.Column(db.Integer, primary_key = True)
    country_name = db.Column(db.String(100))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, country_name):
        self.country_name = country_name

class CountrySchema(marsh.Schema):
    class Meta:
        fields = ('country_name', 'date')


country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)


@app.route('/get', methods = ['GET'])
def get_countries():
    all_countries = Countries.query.all()
    result = countries_schema.dump(all_countries)
    return jsonify(result)


@app.route('/get/<id>/', methods = ['GET'])
def post_country_details(id):
    country = Countries.query.get(id)
    return country_schema.jsonify(country)


@app.route('/add', methods = ['POST'])
def get_country():
    country_name = request.json['country_name']

    countries = Countries(country_name)
    db.session.add(countries)
    db.session.commit()
    return country_schema.jsonify(countries)


@app.route('/update/<id>/', methods = ['PUT'])
def update_country(id):
    country = Countries.query.get(id)

    country_name = request.json['country_name']

    country.country_name = country_name

    db.session.commit()
    return country_schema.jsonify(country)


@app.route('/delete/<id>/', methods = ['DELETE'])
def country_delete(id):
    country = Countries.query.get(id)
    db.session.delete(country)
    db.session.commit()

    return country_schema.jsonify(country)


#  Province --------------------------------------------------------------

class Provinces(db.Model):
    __tablename__ = "province"
    province_id = db.Column(db.Integer, primary_key = True)
    province_name = db.Column(db.String(100))
    country_id = db.Column(db.Integer, ForeignKey("country.country_id"))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, province_name, country_id):
        self.province_name = province_name
        self.country_id = country_id

class ProvinceSchema(marsh.Schema):
    class Meta:
        fields = ('province_name','country_id', 'date')


province_schema = ProvinceSchema()
provinces_schema = ProvinceSchema(many=True)


@app.route('/get', methods = ['GET'])
def get_provinces():
    all_provinces = Provinces.query.all()
    result = provinces_schema.dump(all_provinces)
    return jsonify(result)


@app.route('/get/<id>/', methods = ['GET'])
def post_province_details(id):
    province = Provinces.query.get(id)
    return province_schema.jsonify(province)


@app.route('/add', methods = ['POST'])
def get_province():
    province_name = request.json['province_name']
    country_id = request.json['country_id']

    provinces = Provinces(province_name, country_id)
    db.session.add(provinces)
    db.session.commit()
    return province_schema.jsonify(provinces)


@app.route('/update/<id>/', methods = ['PUT'])
def update_province(id):
    province = Provinces.query.get(id)

    province_name = request.json['province_name']
    country_id = request.json['country_id']

    province.province_name = province_name
    province.country_id = country_id

    db.session.commit()
    return province_schema.jsonify(province)


@app.route('/delete/<id>/', methods = ['DELETE'])
def province_delete(id):
    province = Provinces.query.get(id)
    db.session.delete(province)
    db.session.commit()

    return province_schema.jsonify(province)



#  Plant --------------------------------------------------------------

class Plants(db.Model):
    __tablename__ = "plant"
    plant_id = db.Column(db.Integer, primary_key = True)
    plant_name = db.Column(db.String(100))
    province_id = db.Column(db.Integer, ForeignKey("province.province_id"))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, plant_name, province_id):
        self.plant_name = plant_name
        self.province_id = province_id

class PlantSchema(marsh.Schema):
    class Meta:
        fields = ('plant_name','province_id', 'date')


plant_schema = PlantSchema()
plants_schema = PlantSchema(many=True)


@app.route('/get', methods = ['GET'])
def get_plants():
    all_plants = Plants.query.all()
    result = plants_schema.dump(all_plants)
    return jsonify(result)


@app.route('/get/<id>/', methods = ['GET'])
def post_plant_details(id):
    plant = Plants.query.get(id)
    return plant_schema.jsonify(plant)


@app.route('/add', methods = ['POST'])
def get_plant():
    plant_name = request.json['plant_name']
    province_id = request.json['province_id']

    plants = Plants(plant_name, province_id)
    db.session.add(plants)
    db.session.commit()
    return plant_schema.jsonify(plants)


@app.route('/update/<id>/', methods = ['PUT'])
def update_plant(id):
    plant = Plants.query.get(id)

    plant_name = request.json['plant_name']
    province_id = request.json['province_id']

    plant.plant_name = plant_name
    plant.province_id = province_id

    db.session.commit()
    return plant_schema.jsonify(plant)


@app.route('/delete/<id>/', methods = ['DELETE'])
def plant_delete(id):
    plant = Plants.query.get(id)
    db.session.delete(plant)
    db.session.commit()

    return plant_schema.jsonify(plant)


#  Process --------------------------------------------------------------

class Processes(db.Model):
    __tablename__ = "process"
    process_id = db.Column(db.Integer, primary_key = True)
    process_name = db.Column(db.String(100))
    plant_id = db.Column(db.Integer, ForeignKey("plant.plant_id"))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, process_name, plant_id):
        self.process_name = process_name
        self.plant_id = plant_id

class ProcessSchema(marsh.Schema):
    class Meta:
        fields = ('process_name','plant_id', 'date')


process_schema = ProcessSchema()
processes_schema = ProcessSchema(many=True)


@app.route('/get', methods = ['GET'])
def get_processes():
    all_processes = Processes.query.all()
    result = processes_schema.dump(all_processes)
    return jsonify(result)


@app.route('/get/<id>/', methods = ['GET'])
def post_process_details(id):
    process = Processes.query.get(id)
    return process_schema.jsonify(process)


@app.route('/add', methods = ['POST'])
def get_process():
    process_name = request.json['process_name']
    plant_id = request.json['plant_id']

    processes = Processes(process_name, plant_id)
    db.session.add(processes)
    db.session.commit()
    return process_schema.jsonify(processes)


@app.route('/update/<id>/', methods = ['PUT'])
def update_process(id):
    process = Processes.query.get(id)

    process_name = request.json['process_name']
    plant_id = request.json['plant_id']

    process.process_name = process_name
    process.plant_id = plant_id

    db.session.commit()
    return process_schema.jsonify(process)


@app.route('/delete/<id>/', methods = ['DELETE'])
def process_delete(id):
    process = Processes.query.get(id)
    db.session.delete(process)
    db.session.commit()

    return process_schema.jsonify(process)



#  ProcessLine --------------------------------------------------------------

class ProcessLines(db.Model):
    __tablename__ = "processline"
    processline_id = db.Column(db.Integer, primary_key = True)
    processline_name = db.Column(db.String(100))
    process_id = db.Column(db.Integer, ForeignKey("process.process_id"))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, processline_name, process_id):
        self.processline_name = processline_name
        self.plant_id = process_id

class ProcessLineSchema(marsh.Schema):
    class Meta:
        fields = ('processline_name','plant_id', 'date')


processline_schema = ProcessLineSchema()
processlines_schema = ProcessLineSchema(many=True)


@app.route('/get', methods = ['GET'])
def get_processlines():
    all_processlines = ProcessLines.query.all()
    result = processlines_schema.dump(all_processlines)
    return jsonify(result)


@app.route('/get/<id>/', methods = ['GET'])
def post_processline_details(id):
    processline = ProcessLines.query.get(id)
    return processline_schema.jsonify(processline)


@app.route('/add', methods = ['POST'])
def get_processline():
    processline_name = request.json['processline_name']
    plant_id = request.json['plant_id']

    processlines = ProcessLines(processline_name, plant_id)
    db.session.add(processlines)
    db.session.commit()
    return processline_schema.jsonify(processlines)


@app.route('/update/<id>/', methods = ['PUT'])
def update_processline(id):
    processline = ProcessLines.query.get(id)

    processline_name = request.json['processline_name']
    plant_id = request.json['plant_id']

    processline.processline_name = processline_name
    processline.plant_id = plant_id

    db.session.commit()
    return processline_schema.jsonify(processline)


@app.route('/delete/<id>/', methods = ['DELETE'])
def processline_delete(id):
    processline = ProcessLines.query.get(id)
    db.session.delete(processline)
    db.session.commit()

    return processline_schema.jsonify(processline)



#  AutonomousMobileRobot --------------------------------------------------------------

class AutonomousMobileRobots(db.Model):
    __tablename__ = "autonomousmobilerobot"
    autonomousmobilerobot_id = db.Column(db.Integer, primary_key = True)
    autonomousmobilerobot_name = db.Column(db.String(100))
    processline_id = db.Column(db.Integer, ForeignKey("processline.processline_id"))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, autonomousmobilerobot_name, processline_id):
        self.autonomousmobilerobot_name = autonomousmobilerobot_name
        self.plant_id = processline_id

class AutonomousMobileRobotSchema(marsh.Schema):
    class Meta:
        fields = ('autonomousmobilerobot_name','processline_id', 'date')


autonomousmobilerobot_schema = AutonomousMobileRobotSchema()
autonomousmobilerobots_schema = AutonomousMobileRobotSchema(many=True)


@app.route('/get', methods = ['GET'])
def get_autonomousmobilerobots():
    all_autonomousmobilerobots = AutonomousMobileRobots.query.all()
    result = autonomousmobilerobots_schema.dump(all_autonomousmobilerobots)
    return jsonify(result)


@app.route('/get/<id>/', methods = ['GET'])
def post_autonomousmobilerobot_details(id):
    autonomousmobilerobot = AutonomousMobileRobots.query.get(id)
    return autonomousmobilerobot_schema.jsonify(autonomousmobilerobot)


@app.route('/add', methods = ['POST'])
def get_autonomousmobilerobot():
    autonomousmobilerobot_name = request.json['autonomousmobilerobot_name']
    processline_id = request.json['processline_id']

    autonomousmobilerobots = AutonomousMobileRobots(autonomousmobilerobot_name, processline_id)
    db.session.add(autonomousmobilerobots)
    db.session.commit()
    return autonomousmobilerobot_schema.jsonify(autonomousmobilerobots)


@app.route('/update/<id>/', methods = ['PUT'])
def update_autonomousmobilerobot(id):
    autonomousmobilerobot = AutonomousMobileRobots.query.get(id)

    autonomousmobilerobot_name = request.json['autonomousmobilerobot_name']
    processline_id = request.json['processline_id']

    autonomousmobilerobot.autonomousmobilerobot_name = autonomousmobilerobot_name
    autonomousmobilerobot.processline_id = processline_id

    db.session.commit()
    return autonomousmobilerobot_schema.jsonify(autonomousmobilerobot)


@app.route('/delete/<id>/', methods = ['DELETE'])
def autonomousmobilerobot_delete(id):
    autonomousmobilerobot = AutonomousMobileRobots.query.get(id)
    db.session.delete(autonomousmobilerobot)
    db.session.commit()

    return autonomousmobilerobot_schema.jsonify(autonomousmobilerobot)



# @app.route('/get', methods = ['GET'])
# def get_articles():
#     return jsonify({"Hello":"Sam"})




if __name__ == "__main__":
    app.run(debug=True)
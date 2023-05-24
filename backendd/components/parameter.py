from setup.structure import db, ForeignKey, datetime, marsh, app, jsonify, request


class Parameters(db.Model):
    __tablename__ = "parameter"
    parameter_id = db.Column(db.Integer, primary_key = True)
    parameter_name = db.Column(db.String(100))
    parameter_unit = db.Column(db.String(100))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, parameter_name, parameter_unit):
        self.parameter_name = parameter_name
        self.parameter_unit = parameter_unit

class ParameterSchema(marsh.Schema):
    class Meta:
        fields = ('parameter_name','parameter_unit', 'date')


parameter_schema = ParameterSchema()
parameters_schema = ParameterSchema(many=True)


@app.route('/get', methods = ['GET'])
def get_parameters():
    all_parameters = Parameters.query.all()
    result = parameters_schema.dump(all_parameters)
    return jsonify(result)


@app.route('/get/<id>/', methods = ['GET'])
def post_parameter_details(id):
    parameter = Parameters.query.get(id)
    return parameter_schema.jsonify(parameter)


@app.route('/add', methods = ['POST'])
def get_parameter():
    parameter_name = request.json['parameter_name']
    parameter_description = request.json['parameter_description']

    parameters = Parameters(parameter_name, parameter_description)
    db.session.add(parameters)
    db.session.commit()
    return parameter_schema.jsonify(parameters)


@app.route('/update/<id>/', methods = ['PUT'])
def update_parameter(id):
    parameter = Parameters.query.get(id)

    parameter_name = request.json['parameter_name']
    parameter_description = request.json['parameter_description']

    parameter.parameter_name = parameter_name
    parameter.parameter_description = parameter_description

    db.session.commit()
    return parameter_schema.jsonify(parameter)


@app.route('/delete/<id>/', methods = ['DELETE'])
def parameter_delete(id):
    parameter = Parameters.query.get(id)
    db.session.delete(parameter)
    db.session.commit()

    return parameter_schema.jsonify(parameter)

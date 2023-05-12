from setup.structure import marsh, jsonify, app, request, AutonomousMobileRobots, db


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
def update_process(id):
    autonomousmobilerobot = AutonomousMobileRobots.query.get(id)

    autonomousmobilerobot_name = request.json['autonomousmobilerobot_name']
    processline_id = request.json['processline_id']

    autonomousmobilerobot.autonomousmobilerobot_name = autonomousmobilerobot_name
    autonomousmobilerobot.processline_id = processline_id

    db.session.commit()
    return autonomousmobilerobot_schema.jsonify(autonomousmobilerobot)


@app.route('/delete/<id>/', methods = ['DELETE'])
def process_delete(id):
    autonomousmobilerobot = AutonomousMobileRobots.query.get(id)
    db.session.delete(autonomousmobilerobot)
    db.session.commit()

    return autonomousmobilerobot_schema.jsonify(autonomousmobilerobot)

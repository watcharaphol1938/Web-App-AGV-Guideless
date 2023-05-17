from setup.structure import db, ForeignKey, datetime, marsh, app, jsonify, request


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

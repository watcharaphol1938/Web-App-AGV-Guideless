from setup.structure import marsh, jsonify, app, request, ProcessLines, db


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
def update_process(id):
    processline = ProcessLines.query.get(id)

    processline_name = request.json['processline_name']
    plant_id = request.json['plant_id']

    processline.processline_name = processline_name
    processline.plant_id = plant_id

    db.session.commit()
    return processline_schema.jsonify(processline)


@app.route('/delete/<id>/', methods = ['DELETE'])
def process_delete(id):
    processline = ProcessLines.query.get(id)
    db.session.delete(processline)
    db.session.commit()

    return processline_schema.jsonify(processline)

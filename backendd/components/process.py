from setup.structure import marsh, jsonify, app, request, Processes, db


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

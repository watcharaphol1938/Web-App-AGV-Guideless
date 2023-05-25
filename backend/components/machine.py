from setup.structure import db, ForeignKey, datetime, marsh, app, jsonify, request


class Machines(db.Model):
    __tablename__ = "machine"
    machine_id = db.Column(db.Integer, primary_key = True)
    machine_name = db.Column(db.String(100))
    machine_description = db.Column(db.String(100))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, machine_name, machine_description):
        self.machine_name = machine_name
        self.machine_description = machine_description

class MachineSchema(marsh.Schema):
    class Meta:
        fields = ('machine_name','machine_description', 'date')


machine_schema = MachineSchema()
machines_schema = MachineSchema(many=True)


@app.route('/get', methods = ['GET'])
def get_machines():
    all_machines = Machines.query.all()
    result = machines_schema.dump(all_machines)
    return jsonify(result)


@app.route('/get/<id>/', methods = ['GET'])
def post_machine_details(id):
    machine = Machines.query.get(id)
    return machine_schema.jsonify(machine)


@app.route('/add', methods = ['POST'])
def get_machine():
    machine_name = request.json['machine_name']
    machine_description = request.json['machine_description']

    machines = Machines(machine_name, machine_description)
    db.session.add(machines)
    db.session.commit()
    return machine_schema.jsonify(machines)


@app.route('/update/<id>/', methods = ['PUT'])
def update_machine(id):
    machine = Machines.query.get(id)

    machine_name = request.json['machine_name']
    machine_description = request.json['machine_description']

    machine.machine_name = machine_name
    machine.machine_description = machine_description

    db.session.commit()
    return machine_schema.jsonify(machine)


@app.route('/delete/<id>/', methods = ['DELETE'])
def machine_delete(id):
    machine = Machines.query.get(id)
    db.session.delete(machine)
    db.session.commit()

    return machine_schema.jsonify(machine)

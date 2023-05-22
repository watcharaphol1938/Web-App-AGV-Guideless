from setup.structure import db, ForeignKey, datetime, marsh, app, jsonify, request


class Equipments(db.Model):
    __tablename__ = "equipment"
    equipment_id = db.Column(db.Integer, primary_key = True)
    equipment_name = db.Column(db.String(100))
    equipment_description = db.Column(db.String(100))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, equipment_name, equipment_description):
        self.equipment_name = equipment_name
        self.equipment_description = equipment_description

class EquipmentSchema(marsh.Schema):
    class Meta:
        fields = ('equipment_name','equipment_description', 'date')


equipment_schema = EquipmentSchema()
equipments_schema = EquipmentSchema(many=True)


@app.route('/get', methods = ['GET'])
def get_equipments():
    all_equipments = Equipments.query.all()
    result = equipments_schema.dump(all_equipments)
    return jsonify(result)


@app.route('/get/<id>/', methods = ['GET'])
def post_equipment_details(id):
    equipment = Equipments.query.get(id)
    return equipment_schema.jsonify(equipment)


@app.route('/add', methods = ['POST'])
def get_equipment():
    equipment_name = request.json['equipment_name']
    equipment_description = request.json['equipment_description']

    equipments = Equipments(equipment_name, equipment_description)
    db.session.add(equipments)
    db.session.commit()
    return equipment_schema.jsonify(equipments)


@app.route('/update/<id>/', methods = ['PUT'])
def update_equipment(id):
    equipment = Equipments.query.get(id)

    equipment_name = request.json['equipment_name']
    equipment_description = request.json['equipment_description']

    equipment.equipment_name = equipment_name
    equipment.equipment_description = equipment_description

    db.session.commit()
    return equipment_schema.jsonify(equipment)


@app.route('/delete/<id>/', methods = ['DELETE'])
def equipment_delete(id):
    equipment = Equipments.query.get(id)
    db.session.delete(equipment)
    db.session.commit()

    return equipment_schema.jsonify(equipment)

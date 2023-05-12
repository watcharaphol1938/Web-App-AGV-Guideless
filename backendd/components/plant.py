from setup.structure import marsh, jsonify, app, request, Plants, db


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

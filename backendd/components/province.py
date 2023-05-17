from setup.structure import db, ForeignKey, datetime, marsh, app, jsonify, request


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

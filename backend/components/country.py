from setup.structure import db, datetime, marsh, app, jsonify, request


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
    country_id = request.json['country_id']
    country_name = request.json['country_name']

    countries = Countries(country_id, country_name)
    db.session.add(countries)
    db.session.commit()
    return country_schema.jsonify(countries)


@app.route('/update/<id>/', methods = ['PUT'])
def update_country(id):
    country = Countries.query.get(id)

    country_id = request.json['country_id']
    country_name = request.json['country_name']

    country.country_id = country_id
    country.country_name = country_name

    db.session.commit()
    return country_schema.jsonify(country)


@app.route('/delete/<id>/', methods = ['DELETE'])
def country_delete(id):
    country = Countries.query.get(id)
    db.session.delete(country)
    db.session.commit()

    return country_schema.jsonify(country)

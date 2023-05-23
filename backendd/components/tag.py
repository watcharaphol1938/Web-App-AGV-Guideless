from setup.structure import db, ForeignKey, datetime, marsh, app, jsonify, request


class Tags(db.Model):
    __tablename__ = "tag"
    tag_id = db.Column(db.Integer, primary_key = True)
    tag_name = db.Column(db.String(100))
    tag_reg = db.Column(db.String(100))
    tag_machine = db.Column(db.String(100))
    tag_equipment_name = db.Column(db.String(100))
    tag_equipment_type = db.Column(db.String(100))
    tag_parameter = db.Column(db.String(100))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, tag_name, tag_reg, tag_machine, tag_equipment_name, tag_equipment_type, tag_parameter):
        self.tag_name = tag_name
        self.tag_reg = tag_reg
        self.tag_machine = tag_machine
        self.tag_equipment_name = tag_equipment_name
        self.tag_equipment_type = tag_equipment_type
        self.tag_parameter = tag_parameter

class TagSchema(marsh.Schema):
    class Meta:
        fields = ('tag_name','tag_reg', 'tag_machine', 'tag_equipment_name', 'tag_equipment_type', 'tag_parameter', 'date')


tag_schema = TagSchema()
tags_schema = TagSchema(many=True)


@app.route('/get', methods = ['GET'])
def get_tags():
    all_tags = Tags.query.all()
    result = tags_schema.dump(all_tags)
    return jsonify(result)


@app.route('/get/<id>/', methods = ['GET'])
def post_tag_details(id):
    tag = Tags.query.get(id)
    return tag_schema.jsonify(tag)


@app.route('/add', methods = ['POST'])
def get_tag():
    tag_name = request.json['tag_name']
    tag_reg = request.json['tag_reg']
    tag_machine = request.json['tag_machine']
    tag_equipment_name = request.json['tag_equipment_name']
    tag_equipment_type = request.json['tag_equipment_type']
    tag_parameter = request.json['tag_parameter']

    tags = Tags(tag_name, tag_reg, tag_machine, tag_equipment_name, tag_equipment_type, tag_parameter)
    db.session.add(tags)
    db.session.commit()
    return tag_schema.jsonify(tags)


@app.route('/update/<id>/', methods = ['PUT'])
def update_tag(id):
    tag = Tags.query.get(id)

    tag_name = request.json['tag_name']
    tag_reg = request.json['tag_reg']
    tag_machine = request.json['tag_machine']
    tag_equipment_name = request.json['tag_equipment_name']
    tag_equipment_type = request.json['tag_equipment_type']
    tag_parameter = request.json['tag_parameter']

    tag.tag_name = tag_name
    tag.tag_reg = tag_reg
    tag.tag_machine = tag_machine
    tag.tag_equipment_name = tag_equipment_name
    tag.tag_equipment_type = tag_equipment_type
    tag.tag_parameter = tag_parameter

    db.session.commit()
    return tag_schema.jsonify(tag)


@app.route('/delete/<id>/', methods = ['DELETE'])
def tag_delete(id):
    tag = Tags.query.get(id)
    db.session.delete(tag)
    db.session.commit()

    return tag_schema.jsonify(tag)

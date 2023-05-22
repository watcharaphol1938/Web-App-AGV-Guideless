from setup.structure import db, datetime, marsh, app, jsonify, request
from werkzeug.security import generate_password_hash

class Users(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key = True)
    user_first_name = db.Column(db.String(100))
    user_last_name = db.Column(db.String(100))
    user_remark = db.Column(db.String(100))
    user_email = db.Column(db.String(100))
    user_password = db.Column(db.String(100))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, user_first_name, user_last_name, user_remark, user_email, user_password):
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_remark = user_remark
        self.user_email = user_email
        self.user_password = user_password


class UserSchema(marsh.Schema):
    class Meta:
        fields = ('user_first_name', 'user_last_name', 'user_remark', 'user_email', 'user_password', 'date')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/get', methods = ['GET'])
def get_users():
    all_users = Users.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


@app.route('/get/<id>/', methods = ['GET'])
def post_user_details(id):
    user = Users.query.get(id)
    return user_schema.jsonify(user)


@app.route('/add', methods = ['POST'])
def get_user():
    user_first_name = request.json['user_first_name']
    user_last_name = request.json['user_last_name']
    user_remark = request.json['user_remark']
    user_email = request.json['user_email']
    user_password = request.json['user_password']

    users = Users(user_first_name, user_last_name, user_remark, user_email, user_password)
    db.session.add(users)
    db.session.commit()
    return user_schema.jsonify(users)


@app.route('/update/<id>/', methods = ['PUT'])
def update_user(id):
    user = Users.query.get(id)

    user_first_name = request.json['user_first_name']
    user_last_name = request.json['user_last_name']
    user_remark = request.json['user_remark']
    user_email = request.json['user_email']
    user_password = request.json['user_password']

    user.user_first_name = user_first_name
    user.user_last_name = user_last_name
    user.user_remark = user_remark
    user.user_email = user_email
    user.user_password = user_password

    db.session.commit()
    return user_schema.jsonify(user)


@app.route('/delete/<id>/', methods = ['DELETE'])
def user_delete(id):
    user = Users.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

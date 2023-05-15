import requests, json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/amrdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)
marsh = Marshmallow(app)

res = requests.get("https://raw.githubusercontent.com/kongvut/thai-province-data/master/api_province.json")
list = json.loads(res.text)
# print(list)

newList = []
for i in list:
    if 'id' in i:
        id = i['id']
    else:
        id = 0
    if 'name_en' in i:
        name = i['name_en']
    else:
        name = ''

    store = {
        ['id']: id,
        ['name'] : name
    }
    newList.append(store)

# print(newList)

sql = "insert into amrdb (id, name)"
value = []
for i in newList:
    val = (i['id'], i['name'])
    value.append(val)

db.session.add(value)
db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
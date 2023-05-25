import pymysql, requests, json, datetime


mydb = pymysql.connect(
    host="127.0.0.1",
    user="root",
    # port= 5000,
    password="",
    database="test"
)

mycursor = mydb.cursor()

res = requests.get("https://raw.githubusercontent.com/jkaninda/world-countries/master/countries.json")
list = json.loads(res.text)

for i in list:
    if "name" in i:
        name = i["name"]
    else:
        name = ""
    if "id" in i:
        partnumber = "T" + str(1000 + i["id"])
    else:
        partnumber = str(0)
    sql = "INSERT INTO task (task_name, part_number, date) VALUES (%s, %s, %s)"
    mycursor.execute(sql, (name, partnumber, datetime.datetime.now()))
    mydb.commit()

mydb.close()
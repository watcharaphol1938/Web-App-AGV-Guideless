from setup.structure import json, pymysql, requests


mydb = pymysql.connect(
    host="127.0.0.1",
    user="root",
    # port= 5000,
    password="",
    database="amrdb"
)

mycursor = mydb.cursor()

res = requests.get("https://raw.githubusercontent.com/kongvut/thai-province-data/master/api_province.json")
list = json.loads(res.text)
# print(list)

TaskTable = "CREATE TABLE Task(ID INT PRIMARY KEY AUTO_INCREMENT, NAME CHAR(100) NOT NULL, PARTNUMBER CHAR(50) NOT NULL)"
mycursor.execute(TaskTable)
mydb.commit()

for i in list:
    if "name" in i:
        name = i["name"]
    else:
        name = ""
    if "id" in i:
        partnumber = "T" + str(1000 + i["id"])
    else:
        partnumber = str(0)
    sql = "INSERT INTO task (name, partnumber) VALUES (%s, %s)"
    mycursor.execute(sql, (name, partnumber))
    mydb.commit()

mydb.close()
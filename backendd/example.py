import pymysql, requests, json

mydb = pymysql.connect(
    host="127.0.0.1",
    user="root",
    # port= 5000,
    password="",
    database="amrdb"
)

mycursor = mydb.cursor()

api = requests.get("https://raw.githubusercontent.com/jkaninda/world-countries/master/countries.json")
data = json.loads(api.text)
for i in data:
    if "id" in i:
        id = i["id"]
    else:
        id = 0
    if "name" in i:
        name = i["name"]
    else:
        name = ""
    print(id, " : " ,name)
#     if "id" in i:
#         partnumber = "T" + str(1000 + i["id"])
#     else:
#         partnumber = str(0)
#     if "name_th" in i:
#         name_th = i["name_th"]
#     else:
#         name_th = str(0)
#     sql = "INSERT INTO task (name_en, name_th, partnumber) VALUES (%s, %s, %s)"
#     mycursor.execute(sql, (name_en, name_th, partnumber))
#     mydb.commit()


res = requests.get("https://raw.githubusercontent.com/kongvut/thai-province-data/master/api_province.json")
list = json.loads(res.text)
# print(list)

# TaskTable = "CREATE TABLE Task(ID INT PRIMARY KEY AUTO_INCREMENT, NAME_TH CHAR(50) NOT NULL, NAME_EN CHAR(50) NOT NULL, PARTNUMBER CHAR(50) NOT NULL)"
# mycursor.execute(TaskTable)
# mydb.commit()

# for i in list:
#     if "name_en" in i:
#         name_en = i["name_en"]
#     else:
#         name_en = ""
#     if "id" in i:
#         partnumber = "T" + str(1000 + i["id"])
#     else:
#         partnumber = str(0)
#     if "name_th" in i:
#         name_th = i["name_th"]
#     else:
#         name_th = str(0)
#     sql = "INSERT INTO task (name_en, name_th, partnumber) VALUES (%s, %s, %s)"
#     mycursor.execute(sql, (name_en, name_th, partnumber))
#     mydb.commit()

# mydb.close()
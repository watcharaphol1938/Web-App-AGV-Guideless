from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Country(Base):
    __tablename__ = "country"
    country_id = Column("country_id", Integer, primary_key=True)
    country_name = Column("country_name", String)

    def __init__(self, country_id, country_name):
        self.country_id = country_id
        self.country_name = country_name

    def __repr__(self):
        return f"({self.country_id}) {self.country_name}"
    
class Province(Base):
    __tablename__ = "province"
    province_id = Column("province_id", Integer, primary_key=True)
    province_name = Column("province_name", String)
    country_id = Column(Integer, ForeignKey("country.country_id"))

    def __init__(self, province_id, province_name, country_id):
        self.province_id = province_id
        self.province_name = province_name
        self.country_id = country_id

    def __repr__(self):
        return f"({self.province_id}) {self.province_name} {self.country_id}"
    
class Plant(Base):
    __tablename__ = "plant"
    plant_id = Column("plant_id", Integer, primary_key=True)
    plant_name = Column("plant_name", String)
    province_id = Column(Integer, ForeignKey("province.province_id"))

    def __init__(self, plant_id, plant_name, province_id):
        self.plant_id = plant_id
        self.plant_name = plant_name
        self.province_id = province_id

    def __repr__(self):
        return f"({self.plant_id}) {self.plant_name} {self.province_id}"
    
class Process(Base):
    __tablename__ = "process"
    process_id = Column("process_id", Integer, primary_key=True)
    process_name = Column("process_name", String)
    plant_id = Column(Integer, ForeignKey("plant.plant_id"))

    def __init__(self, process_id, process_name, plant_id):
        self.process_id = process_id
        self.process_name = process_name
        self.plant_id = plant_id

    def __repr__(self):
        return f"({self.process_id}) {self.process_name} {self.plant_id}"
    
class ProcessLine(Base):
    __tablename__ = "processline"
    processline_id = Column("processline_id", Integer, primary_key=True)
    processline_name = Column("processline_name", String)
    process_id = Column(Integer, ForeignKey("process.process_id"))

    def __init__(self, processline_id, processline_name, process_id):
        self.processline_id = processline_id
        self.processline_name = processline_name
        self.process_id = process_id

    def __repr__(self):
        return f"({self.processline_id}) {self.processline_name} {self.process_id}"
    
class AutonomousMobileRobot(Base):
    __tablename__ = "autonomousmobilerobot"
    autonomousmobilerobot_id = Column("autonomousmobilerobot_id", Integer, primary_key=True)
    autonomousmobilerobot_name = Column("autonomousmobilerobot_name", String)
    processline_id = Column(Integer, ForeignKey("processline.processline_id"))

    def __init__(self, autonomousmobilerobot_id, autonomousmobilerobot_name, processline_id):
        self.autonomousmobilerobot_id = autonomousmobilerobot_id
        self.autonomousmobilerobot_name = autonomousmobilerobot_name
        self.processline_id = processline_id

    def __repr__(self):
        return f"({self.autonomousmobilerobot_id}) {self.autonomousmobilerobot_name} {self.processline_id}"
    
engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# Country ------------------------------------------------------------------------------------------------
country1 = Country(1, "Thailand")
country2 = Country(2, "Japan")
country3 = Country(3, "China")
country4 = Country(4, "South Korea")
session.add(country1)
session.add(country2)
session.add(country3)
session.add(country4)
session.commit()

# Province ------------------------------------------------------------------------------------------------
province1 = Province(1, "Chonburi", country1.country_id)
province2 = Province(2, "Wuhan", country3.country_id)
province3 = Province(3, "Aichi", country2.country_id)
province4 = Province(4, "Gyeonggi", country4.country_id)
session.add(province1)
session.add(province2)
session.add(province3)
session.add(province4)
session.commit()

# Plant ------------------------------------------------------------------------------------------------
plant1 = Plant(1, "SIAM DENSO MANUFACTURING CO., LTD.", province1.province_id)
plant2 = Plant(2, "DENSO KOTEI AUTOMOTIVE ELECTRONICS (WUHAN) CO., LTD", province3.province_id)
plant3 = Plant(3, "Toyohashi Plant", province2.province_id)
plant4 = Plant(4, "KOREA WIPER BLADE CO., LTD.", province4.province_id)
session.add(plant1)
session.add(plant2)
session.add(plant3)
session.add(plant4)
session.commit()

# Process ------------------------------------------------------------------------------------------------
process1 = Process(1, "A", plant1.plant_id)
process2 = Process(2, "B", plant3.plant_id)
process3 = Process(3, "C", plant2.plant_id)
process4 = Process(4, "D", plant4.plant_id)
session.add(process1)
session.add(process2)
session.add(process3)
session.add(process4)
session.commit()

# ProcessLine ------------------------------------------------------------------------------------------------
processline1 = ProcessLine(1, "E", process1.process_id)
processline2 = ProcessLine(2, "F", process3.process_id)
processline3 = ProcessLine(3, "G", process2.process_id)
processline4 = ProcessLine(4, "H", process4.process_id)
session.add(processline1)
session.add(processline2)
session.add(processline3)
session.add(processline4)
session.commit()

# AutonomousMobileRobot ------------------------------------------------------------------------------------------------
autonomousmobilrrobot1 = AutonomousMobileRobot(1, "I", processline1.processline_id)
autonomousmobilrrobot2 = AutonomousMobileRobot(2, "J", processline3.processline_id)
autonomousmobilrrobot3 = AutonomousMobileRobot(3, "K", processline2.processline_id)
autonomousmobilrrobot4 = AutonomousMobileRobot(4, "L", processline4.processline_id)
session.add(autonomousmobilrrobot1)
session.add(autonomousmobilrrobot2)
session.add(autonomousmobilrrobot3)
session.add(autonomousmobilrrobot4)
session.commit()
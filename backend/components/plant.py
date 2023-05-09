from setup.structure import Plant, session
from components.province import province1, province2, province3, province4

plant1 = Plant(1, "SIAM DENSO MANUFACTURING CO., LTD.", province1.province_id)
plant2 = Plant(2, "DENSO KOTEI AUTOMOTIVE ELECTRONICS (WUHAN) CO., LTD", province3.province_id)
plant3 = Plant(3, "Toyohashi Plant", province2.province_id)
plant4 = Plant(4, "KOREA WIPER BLADE CO., LTD.", province4.province_id)
session.add(plant1)
session.add(plant2)
session.add(plant3)
session.add(plant4)
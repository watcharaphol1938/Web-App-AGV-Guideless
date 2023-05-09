from setup.structure import Province, session
from components.country import country1, country2, country3, country4

province1 = Province(1, "Chonburi", country1.country_id)
province2 = Province(2, "Wuhan", country3.country_id)
province3 = Province(3, "Aichi", country2.country_id)
province4 = Province(4, "Gyeonggi", country4.country_id)
session.add(province1)
session.add(province2)
session.add(province3)
session.add(province4)
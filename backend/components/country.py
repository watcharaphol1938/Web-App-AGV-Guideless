from setup.structure import Country, session

country1 = Country(1, "Thailand")
country2 = Country(2, "Japan")
country3 = Country(3, "China")
country4 = Country(4, "South Korea")
session.add(country1)
session.add(country2)
session.add(country3)
session.add(country4)
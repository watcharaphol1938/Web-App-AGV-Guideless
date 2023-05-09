from flask import session
from backend.app import Country

c1 = Country(1, "Thailand")
c2 = Country(2, "Japan")
c3 = Country(3, "China")
c4 = Country(4, "South Korea")
session.add(c1)
session.add(c2)
session.add(c3)
session.add(c4)
session.commit()
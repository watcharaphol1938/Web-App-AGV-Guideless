from components.country import app, db
from components.province import app, db
from components.plant import app, db
from components.process import app, db
from components.processline import app, db
from components.autonomousmobilerobot import app, db
from components.task import app, db


db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
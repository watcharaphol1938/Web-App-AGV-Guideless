from setup.structure import app, db

db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
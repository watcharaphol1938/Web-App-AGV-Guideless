from setup.structure import db, datetime, pymysql, requests, json, app, request, jsonify, marsh


class Tasks(db.Model):
    __tablename__ = "task"
    task_id = db.Column(db.Integer, primary_key = True)
    task_name = db.Column(db.String(100))
    part_number = db.Column(db.String(100))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, task_name, part_number):
        self.task_name = task_name
        self.part_number = part_number


class TaskSchema(marsh.Schema):
    class Meta:
        fields = ('task_name', 'part_number', 'date')


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


@app.route('/get', methods = ['GET'])
def get_tasks():
    all_tasks = Tasks.query.all()
    result = tasks_schema.dump(all_tasks)
    return jsonify(result)
    # return {'result':'ok'}


@app.route('/get/<id>/', methods = ['GET'])
def post_task_details(id):
    task = Tasks.query.get(id)
    return task_schema.jsonify(task)


@app.route('/add', methods = ['POST'])
def get_task():
    task_name = request.json['task_name']

    tasks = Tasks(task_name)
    db.session.add(tasks)
    db.session.commit()
    return task_schema.jsonify(tasks)


@app.route('/update/<id>/', methods = ['PUT'])
def update_task(id):
    task = Tasks.query.get(id)

    task_name = request.json['task_name']

    task.country_name = task_name

    db.session.commit()
    return task_schema.jsonify(task)


@app.route('/delete/<id>/', methods = ['DELETE'])
def task_delete(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()

    return task_schema.jsonify(task)
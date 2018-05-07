from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
import json

import db_interaction

app = Flask(__name__)
Bootstrap(app)

#app.secret_key = "veryveryverysecrettt"

@app.route('/')
def hello_world():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return render_template("index.html", tasks=db_interaction.readTasks())


@app.route('/create_task', methods=['POST'])
def create_task():
    task = request.form['task']
    urgency = request.form['options']
    print(urgency)
    db_interaction.saveTask(task, urgency)
    return render_template("create_task.html")


@app.route('/delete_task/<id_task>')
def delete_task(id_task):
    tasks = db_interaction.readTasks()
    db_interaction.removeTask(id_task)
    task = [task for task in tasks if task[0] == id_task]
    return render_template("delete_task.html", task=task)


if __name__ == '__main__':
    app.run()

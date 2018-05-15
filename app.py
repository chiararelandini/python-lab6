from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
import json

import db_interaction

app = Flask(__name__)
Bootstrap(app)

#app.secret_key = "veryveryverysecrettt"

@app.route('/')
def hello_world():
    return redirect(url_for('tasks'))


@app.route('/tasks')
def ListTasks():
    #return render_template("index.html", tasks=db_interaction.readTasks())
    tasks = db_interaction.readTasks()
    return jsonify(tasks)


@app.route('/tasks', methods=['POST'])
def CreateTask():
    new_task = request.json
    #new_task is a dictionary containing all info (passed by client api)
    todo = new_task['todo']
    urgency = new_task['urgency']
    #check new_task does not exist yet
    tasks = db_interaction.readTasks() #returns a list of list
    for task in tasks:
        if task[1] == todo:
            #task already existing (?) --- urgency could be different; id_task is the unique key
            response = jsonify({"message": "task already existing!"})  # jsonify fake json with error message
            response.status_code = 404  # http message
            return response
    db_interaction.saveTask(todo, urgency)
    return jsonify(new_task)


@app.route('/tasks/<id_task>', methods=['DELETE'])
def DeleteTask(id_task):
    # print("DELETEEEE")
    # tasks = db_interaction.readTasks()
    # print(tasks)
    # print(id_task)
    # #id_task = request.json
    # # task = [task for task in tasks if task[0] == id_task]
    # delete_task = ''
    # for task in tasks:
    #     print(task[0])
    #     if task[0]==id_task:
    #         delete_task = task
    # print("task to remove:")
    # print(delete_task)
    # if(delete_task!=''):
    #     db_interaction.removeTask(id_task)
    #     return jsonify(delete_task)
    # else:
    #     response = jsonify({"message": "task "+id_task+" not found!"})  # jsonify fake json with error message
    #     response.status_code = 404  # http message
    #     return response
    db_interaction.removeTask(id_task)
    return jsonify(id_task)


@app.route('/tasks/<id_task>', methods=['PUT'])
def UpdateTask():   #update[0] = tod_o and update[1]= urgency
    # tasks = db_interaction.readTasks()
    # task = [task for task in tasks if task[0] == id_task]
    # # update task
    # if (len(task) == 1):
    #     db_interaction.updateTask(id_task, update)
    #     return jsonify(update)
    # else:
    #     response = jsonify({"message": "task " + id_task + " not found!"})  # jsonify fake json with error message
    #     response.status_code = 404  # http message
    #     return response
    update = request.data
    db_interaction.updateTask(update[0], update)
    return jsonify(update)


@app.route('/tasks/<id_task>')
def GetTask(id_task):
    task = db_interaction.retrieveTask(int(id_task))
    print(task)
    if len(task)==0:
        return jsonify(task[0])
    else:
        response = jsonify({"message":"duplicated task with the id "+id_task})
        response.status_code = 404
        return response


if __name__ == '__main__':
    app.run()
import pymysql


#import the list of tasks from the database
def readTasks():
    sql = "SELECT * from task"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="todomanager")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    #tasks = []
    #for task in result:
        #print(task[1])
        #tasks.append(task[1])
    #print(result)
    cursor.close()
    connection.close()
    return result


def saveTask(newTask, urgency):
    sql = "INSERT into task(description, urgency) VALUES (%s, %s)"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="todomanager")
    cursor = connection.cursor()
    if urgency == "urgent":
        bool_urgency = True
    else:
        bool_urgency = False
    cursor.execute(sql, (newTask, bool_urgency))
    connection.commit()
    cursor.close()
    connection.close()


def removeTask(id_task):
    sql = "DELETE FROM task WHERE id=%s"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="todomanager")
    cursor = connection.cursor()
    cursor.execute(sql, (id_task,))
    connection.commit()
    cursor.close()
    connection.close()


def updateTask(task):
    connection = pymysql.connect(user="root", password="root", host="localhost", database="todomanager")
    cursor = connection.cursor()
    if len(task)==3:
        sql = "UPDATE task SET description=%s, urgency=%s WHERE id=%s"
        if task[2] == "urgent":
            urgency = True
        else:
            urgency = False
        cursor.execute(sql, (task[1], urgency, task[0]))
    else:
        sql = "UPDATE task SET description=%s WHERE id=%s"
        cursor.execute(sql, (task[1], task[0]))
    connection.commit()
    cursor.close()
    connection.close()


def retrieveTask(id_task):
    print("id = "+ str(id_task))
    sql = "SELECT * from task WHERE id=%s"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="todomanager")
    cursor = connection.cursor()
    cursor.execute(sql, (id_task,))
    result = cursor.fetchall()
    print(result)
    cursor.close()
    connection.close()
    return result
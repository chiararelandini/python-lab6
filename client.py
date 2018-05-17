import requests


base_url = 'http://localhost:5000'


def queryAPI():
    tasks = requests.get(base_url + '/tasks').json()
    print("List of tasks:")
    print(tasks)

    # add a task
    # todo = "invitare Albiiiiii"
    # urgency = "urgent"
    # new_task = {'todo': todo, 'urgency': urgency}
    #
    # requests.post(base_url + '/tasks', json=new_task)

    #remove a task
    # num = 7
    # requests.delete(base_url+ '/tasks/' + str(num), json=num)

    #update a task ----- NOT WORKING !!!!
    # id = 7
    # description = "andare in palestra"
    # update = [id, description]
    # requests.put(base_url+"/tasks/"+str(id), data=update, json=id)
    #
    id = 2
    description = "fare la spesa"
    update = [id, description, "not urgent"]
    requests.put(base_url + "/tasks/" + str(id), data=None, json={"update": update, "id_task": str(id)})

    #retrieve a task
    id = 2
    retrieve = requests.get(base_url+"/tasks/"+str(id)).json()
    print("retrieved")
    print(retrieve)

    tasks = requests.get(base_url + '/tasks').json()
    print("List of tasks:")
    print(tasks)


if __name__=="__main__":
    queryAPI()
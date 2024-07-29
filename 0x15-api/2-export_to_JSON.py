#!/usr/bin/python3
""" Get Employee info """

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    if len(argv) < 2:
        exit(1)

    id = argv[1]
    url_info = f"https://jsonplaceholder.typicode.com/users/{id}"
    url_toDo = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    r = requests.get(url_info)
    rd = requests.get(url_toDo)

    content_info = r.json()
    content_todo = rd.json()
    user_id = content_info.get('id')

    file_name = f"{user_id}.json"
    data = {}
    user_id = content_info.get('id')
    u_name = content_info.get('username')
    data[user_id] = []
    user_tasks = [t for t in content_todo if t['userId'] == user_id]
    for task in user_tasks:
        task_info = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": u_name
            }
        data[user_id].append(task_info)
    with open(file_name, mode='w') as file:
        json.dump(data, file)

#!/usr/bin/python3
""" Get Employee info """

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    url_info = f"https://jsonplaceholder.typicode.com/users/"
    url_toDo = f"https://jsonplaceholder.typicode.com/todos"

    r = requests.get(url_info)
    rd = requests.get(url_toDo)

    content_info = r.json()
    content_todo = rd.json()

    file_name = "todo_all_employees.json"
    data = {}
    for user in content_info:
        user_id = user.get('id')
        u_name = user.get('username')
        data[user_id] = []

        user_tasks = [t for t in content_todo if t['userId'] == user_id]
        for task in user_tasks:
            task_info = {
                "username": u_name,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            data[user_id].append(task_info)
    with open(file_name, mode='w') as file:
        json.dump(data, file)

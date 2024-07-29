#!/usr/bin/python3
""" Get Employee info """

if __name__ == "__main__":
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
    name = content_info.get('name')
    do_tasks = 0
    for item in content_todo:
        if item.get('completed'):
            do_tasks += 1
    s = f"Employee {name} is done with tasks({do_tasks}/{len(content_todo)}):"
    print(s)
    for item in content_todo:
        if item.get('completed'):
            task_name = item.get('title')
            print(f"\t {task_name}")

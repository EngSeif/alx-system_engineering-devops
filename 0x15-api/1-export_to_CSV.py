#!/usr/bin/python3
""" Get Employee info """

if __name__ == "__main__":
    import csv
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
    name = content_info.get('username')
    user_id = content_info.get('id')
    file_name = f"{user_id}.csv"
    with open(file_name, mode='w', newline='\n') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in content_todo:
            writer.writerow([user_id, name, todo['completed'], todo['title']])

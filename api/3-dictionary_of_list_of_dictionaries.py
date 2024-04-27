#!/usr/bin/python3
"""
Extends the Python script to fetch and export
all tasks for all employees in JSON format.
Records all tasks that are owned by each employee.
Format must be: { "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ], ... }
File name must be: todo_all_employees.json
"""

from sys import argv
from requests import get
from json import dump

url_base = 'https://jsonplaceholder.typicode.com/users/'


def dict_of_the_dict():
    """
        Fetches and exports all tasks for
        all employees in JSON format.

    Returns:
        None
    """
    users = get(url_base).json()
    retrieve_json = dict()

    for user in users:
        usr_id = user['id']
        item_data = []
        task_users = get(url_base + str(usr_id) + '/todos/').json()

        for todo in task_users:
            item_dict = {
                'task': todo['title'],
                'completed': todo['completed'],
                'username': user['username']
            }
            item_data.append(item_dict)
        retrieve_json[usr_id] = item_data

    with open('todo_all_employees.json', 'w', encoding='utf-8') as file_json:
        dump(retrieve_json, file_json)


if __name__ == '__main__':
    dict_of_the_dict()

#!/usr/bin/python3
"""
Extends the Python script to export data in JSON format.
Records all tasks that are owned by this employee.
Format must be: { "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""

from sys import argv
from json import dump
from requests import get

url_base = 'https://jsonplaceholder.typicode.com/users/'


def export_json(id):
    """
    Fetches the tasks owned by a given employee ID
    and exports them to a JSON file.
    Each record in the JSON file contains the following fields:
    - task: The title of the task
    - completed: The completion status of the task
    - username: The username of the employee

    Args:
        employee_id (int): The ID of the employee
        whose tasks need to be exported.

    Returns:
        None
    """

    file_name = str(id) + '.json'
    usr = get(url_base + str(id)).json()
    todos = get(url_base + str(id) + '/todos/').json()
    items_data = []
    retrieve_json = dict()

    for todo in todos:
        item_dict = dict()
        item_dict['task'] = todo['title']
        item_dict['completed'] = todo['completed']
        item_dict['username'] = usr['username']
        items_data.append(item_dict)

    retrieve_json[str(id)] = items_data

    with open(file_name, 'w', encoding='utf-8') as file_json:
        dump(retrieve_json, file_json)


if __name__ == '__main__':
    export_json(int(argv[1]))

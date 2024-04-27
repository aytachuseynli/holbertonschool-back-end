#!/usr/bin/python3
"""
Extends the Python script to export data in CSV format.
Records all tasks that are owned by this employee.
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

from sys import argv
from requests import get

url_base = 'https://jsonplaceholder.typicode.com/users/'


def export_csv():
    """
    Fetches the tasks owned by a given employee ID and exports them to a CSV file.
    Each record in the CSV file contains the following fields:
    - USER_ID
    - USERNAME
    - TASK_COMPLETED_STATUS
    - TASK_TITLE

    Returns:
        None
    """
    usr = get(url_base + argv[1]).json()
    tasks = get(url_base + argv[1] + '/todos').json()
    file_name = argv[1] + '.csv'

    for task in tasks:
        data = '"' + str(usr['id']) + '",' + '"' + usr['username'] + '",' +\
               '"' + str(task['completed']) + '",' + '"' + task['title'] +\
               '"\n'

        with open(file_name, 'a', encoding='utf-8') as csvfile:
            csvfile.write(data)


if __name__ == '__main__':
    export_csv()
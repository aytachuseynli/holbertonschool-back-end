#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

url_base = 'https://jsonplaceholder.typicode.com/users/'


def get_employee_todo_progress(employee_id):
    """
    Fetches the TODO list progress for a given employee ID and prints it to
    standard output.

    Args:
        employee_id (int): The ID of the employee whose TODO list progress
                           needs to be fetched.

    Returns:
        None
    """
    name = requests.get(url_base + str(employee_id)).json()
    todos = requests.get(url_base + str(employee_id) + '/todos/').json()
    count = 0
    title = ""

    for item in todos:
        if item['completed'] is True:
            title += "\t{}\n".format(item['title'])
            count += 1

    print("Employee {} is done with tasks ({}/20):\n{}".format(name['name'],
                                                                count, title),
        end='')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    get_employee_todo_progress(int(sys.argv[1]))

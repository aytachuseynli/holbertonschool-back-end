#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
from sys import argv

url_base = 'https://jsonplaceholder.typicode.com/users/'


def get_employee_todo_progress(employee_id):
    """
    Fetches the TODO list progress for a given employee ID and
    prints it to standard output.

    Args:
        employee_id (int): The ID of the employee whose
        TODO list progress needs to be fetched.

    Returns:
        None
    """
    name = requests.get(url_base + argv[1]).json()
    todos = requests.get(url_base + argv[1] + '/todos/').json()
    count = 0
    title = ""

    for item in todos:
        if item['completed'] is True:
            title += "\t{}\n".format(item['title'])
            count += 1

    print("Employee {} is done with tasks({}/20):\n{}".format(
        name['name'], count, title), end='')


if __name__ == "__main__":
    get_employee_todo_progress()

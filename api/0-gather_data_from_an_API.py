#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


import requests
import sys


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
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos = requests.get(url).json()
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    print(
        f"Employee {todos[0]['name']} is done with tasks "
        f"({len(completed_tasks)}/{len(todos)}):"
    )
    for task in completed_tasks:
        print(f"\t{task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    get_employee_todo_progress(int(sys.argv[1]))

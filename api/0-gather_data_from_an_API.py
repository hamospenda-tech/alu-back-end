#!/usr/bin/python3
"""Gather an employee's TODO list progress from a REST API.

Usage: ./0-gather_data_from_an_API.py <employee_id>
"""
import requests
import sys


USERS_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"


def get_todo_progress(employee_id):
    """Print the TODO list progress of the employee with the given ID."""
    users = requests.get(USERS_URL).json()
    todos = requests.get(TODOS_URL).json()

    employee_name = None
    for user in users:
        if user.get("id") == employee_id:
            employee_name = user.get("name")

    employee_todos = [
        task for task in todos if task.get("userId") == employee_id
    ]
    done_tasks = [task for task in employee_todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), len(employee_todos)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    get_todo_progress(int(sys.argv[1]))

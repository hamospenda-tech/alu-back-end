#!/usr/bin/python3
"""Gather an employee's TODO list progress from a REST API.

Usage: ./0-gather_data_from_an_API.py <employee_id>
"""
import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


def get_todo_progress(employee_id):
    """Print the TODO list progress of the employee with the given ID."""
    user = requests.get("{}/users/{}".format(API_URL, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(API_URL), params={"userId": employee_id}
    ).json()

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), len(todos)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    get_todo_progress(int(sys.argv[1]))

#!/usr/bin/python3
"""Display an employee's TODO list progress using a REST API."""
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos?userId={}".format(base_url, employee_id)).json()

    done_titles = [t["title"] for t in todos if t["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(done_titles), len(todos)))
    for title in done_titles:
        print("\t {}".format(title))

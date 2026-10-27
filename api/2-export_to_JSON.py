#!/usr/bin/python3
"""Export an employee's TODO list data to a JSON file."""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}
    ).json()

    username = user.get("username")
    data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
            for task in todos
        ]
    }

    with open("{}.json".format(employee_id), "w") as f:
        json.dump(data, f)

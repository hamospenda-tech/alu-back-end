#!/usr/bin/python3
"""Export the TODO lists of all employees to a JSON file."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(url)).json()
    data = {}
    for user in users:
        user_id = user.get("id")
        todos = requests.get("{}/todos".format(url),
                             params={"userId": user_id}).json()
        data[str(user_id)] = [{"username": user.get("username"),
                               "task": t.get("title"),
                               "completed": t.get("completed")}
                              for t in todos]
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)

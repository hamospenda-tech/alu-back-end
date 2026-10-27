#!/usr/bin/python3
"""Export all employees' TODO list data to a single JSON file."""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{base_url}/users").json()
    todos = requests.get(f"{base_url}/todos").json()

    data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        data[str(user_id)] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in todos
            if task.get("userId") == user_id
        ]

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)

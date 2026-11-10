#!/usr/bin/python3
"""Export the TODO list of an employee to a CSV file."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get("{}/users/{}".format(url, user_id)).json()
    todos = requests.get("{}/todos".format(url),
                         params={"userId": user_id}).json()
    username = user.get("username")
    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get("completed"),
                             task.get("title")])

#!/usr/bin/python3
"""Display an employee's TODO list progress using a REST API."""
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}
    ).json()

    done_titles = [t["title"] for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_titles), len(todos)))
    for title in done_titles:
        print("\t {}".format(title))

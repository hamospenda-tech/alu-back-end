#!/usr/bin/python3
"""Display an employee's TODO list progress using a REST API."""
import json
import sys
import urllib.request


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = fetch("{}/users/{}".format(base_url, employee_id))
    todos = fetch("{}/todos?userId={}".format(base_url, employee_id))

    done_titles = [t["title"] for t in todos if t["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(done_titles), len(todos)))
    for title in done_titles:
        print("\t {}".format(title))

#!/usr/bin/python3

"""Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    name = response.json().get("name")

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    response = requests.get(url)
    tasks = response.json()

    completed_tasks = []
    for task in tasks:
        if task.get("completed"):
            completed_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task))

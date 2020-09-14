#!/usr/bin/python3
"""This module is in charge of making the connection with the api and
    export the information about a employee TODO list progress to json."""
import json
import requests
from sys import argv


def connection():
    """This method is responsible for making the connection with the api
        and decoding the json format.

    Returns:
        dict: Users and tasks in dictionary format.
    """
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    return tasks.json(), users.json()


def to_json(employee_id, dictionary):
    """This method is responsible for exporting the information to json format.

    Args:
        employee_id (int): User identifier number.
        dictionay (dict): All formated information.
    """
    with open("{}.json".format(employee_id), "w") as file:
        json.dump(dictionary, file)


def main_function(employee_id):
    """This method is in charge of processing the task and user
        dictionaries to convert to useful information.

    Args:
        employee_id (int): User identifier number.
    """
    if not employee_id.isdigit():
        return

    employee_id = int(employee_id)
    tasks_content, users_content = connection()

    for user in users_content:
        if user.get("id") == employee_id:
            break
    else:
        return

    tasks_list = []
    for task in tasks_content:
        if task.get("userId") == employee_id:
            tasks_list.append({"task": task.get("title"),
                               "completed": task.get("completed"),
                               "username": user.get("name")})
    if len(tasks_list) == 0:
        return

    dictionary = {}
    dictionary[employee_id] = tasks_list

    to_json(employee_id, dictionary)


if __name__ == '__main__':
    main_function(argv[1])

#!/usr/bin/python3
"""This module is in charge of making the connection with the api and
    export the information about a employee TODO list progress to csv."""
import csv
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


def to_csv(user, tasks_content):
    """This method is responsible for exporting the information to csv format.

    Args:
        user (dict): Employee.
        tasks_content (list): List of users tasks.
    """
    with open("{}.csv".format(user.get("id")), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in tasks_content:
            if task.get("userId") == user.get("id"):
                writer.writerow([user.get("id"), user.get("name"),
                                task.get("completed"), task.get("title")])


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

    for task in tasks_content:
        if task.get("userId") == employee_id:
            break
    else:
        return

    to_csv(user, tasks_content)


if __name__ == '__main__':
    if len(argv) == 2:
        main_function(argv[1])

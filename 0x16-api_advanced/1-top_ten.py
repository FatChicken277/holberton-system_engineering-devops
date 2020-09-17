#!/usr/bin/python3
"""This module is in charge of making the connection with the api and prints
    the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """This method prints the titles of the first 10 hot posts listed
        for a given subreddit."""
    headers = {"user-agent": "1637-holberton"}
    r = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.format(
        subreddit), headers=headers)
    if r.status_code != 200:
        print(None)
        return
    for child in r.json().get("data").get("children")[:10]:
        print(child.get("data").get("title"))

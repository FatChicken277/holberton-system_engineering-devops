#!/usr/bin/python3
"""This module is in charge of making the connection with the api
    and return the number of subscribers of a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """This method returns the number of subscribers of a given subreddit"""
    headers = {"user-agent": "1637-holberton"}
    response = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=headers).json()
    if response.get("data") and response.get("data").get("subscribers"):
        return response.get("data").get("subscribers")
    return 0

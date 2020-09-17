#!/usr/bin/python3
"""This Module is responsible for returns a list containing the titles of
    all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """This method returns a list containing the titles of all
        hot articles for a given subreddit"""
    headers = {"user-agent": "1637-holberton"}
    if after is None:
        return hot_list
    if after == "":
        r = requests.get('https://www.reddit.com/r/{}/hot.json'.format(
            subreddit), headers=headers, allow_redirects=False)
    else:
        r = requests.get(
            'https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after), headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None
    after = r.json().get("data").get("after")
    for child in r.json().get("data").get("children")[:10]:
        hot_list.append(child.get("data").get("title"))
    return recurse(subreddit, hot_list, after)

#!/usr/bin/python3
"""This module is in charge of making the connection with the
    api and parses the title of all hot articles, and prints a
    sorted count of given keywords."""
import requests
from collections import OrderedDict


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
    for child in r.json().get("data").get("children"):
        hot_list.append(child.get("data").get("title"))
    return recurse(subreddit, hot_list, after)


def count_words(subreddit, word_list):
    """This method parses the title of all hot articles,
        and prints a sorted count of given keywords."""
    titles = recurse(subreddit)
    if titles is None:
        return
    dictionary = OrderedDict()
    for word in word_list:
        all_sum = sum(word in title for title in titles)
        if all_sum > 0:
            dictionary[word] = all_sum
    dictionary = sorted(dictionary.items(), key=lambda x: x[0])
    for k, v in sorted(dictionary, key=lambda x: x[1], reverse=True):
        print("{}: {}".format(k, v))

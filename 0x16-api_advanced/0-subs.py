#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers)
"""
import requests


def number_of_subscribers(subreddit):
    """
    e a function that queries the Reddit API and
    returns the number of subscribers
    """
    url = f"https://api.reddit.com/r/{subreddit}/about/"
    r = requests.get(url, allow_redirects=False)
    if r.status_code == 200:
        data =  r.json().get("data", {})
        return data.get("subscribers", 0)
    return 0

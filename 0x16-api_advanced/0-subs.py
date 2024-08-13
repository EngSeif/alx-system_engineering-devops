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
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'myRedditApp/1.0'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code < 300:
        data = r.json().get("data", {})
        return data.get("subscribers", 0)
    return 0

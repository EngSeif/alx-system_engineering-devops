#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API
    and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'request'}
    params = {'limit': 10}
    r = requests.get(url,
                     headers=headers,
                     params=params,
                     allow_redirects=False)
    if r.status_code < 300:
        data = r.json().get("data", {}).get("children")
        for d in data:
            print(d.get('data').get('title'))
    return None

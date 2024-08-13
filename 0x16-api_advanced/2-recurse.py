#!/usr/bin/python3
"""
a recursive function that queries the Reddit
API and returns a list containing the titles
of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    a recursive function that queries the Reddit
    API and returns a list containing the titles
    of all hot articles
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'request'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    r = requests.get(url,
                     headers=headers,
                     params=params,
                     allow_redirects=False)
    if r.status_code < 300:
        data = r.json().get("data", {}).get("children")
        if not data:
            return hot_list
        for d in data:
            hot_list.append(d.get('data').get('title'))
        after = r.json().get('data', {}).get('after', None)
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    return None

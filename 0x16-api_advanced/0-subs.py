#!/usr/bin/python3
# function that queries the Reddit API and returns the number of subscribers
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of Subscribers
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    # Request
    req = requests.get('http://www.reddit.com/r/{}/about.json\
'.format(subreddit), headers={
                            'User-Agent': '0x16-api_advanced:project: v1.0.0\
(by /u/kinyarasam)'}).json()

    # Get subs.
    subs = req.get("data", {}).get("subscribers", 0)
    return subs

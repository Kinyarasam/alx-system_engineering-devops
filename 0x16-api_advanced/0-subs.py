#!/usr/bin/python3
# function that queries the Reddit API and returns the number of subscribers
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of Subscribers

    Returns:
        (int) number of subscribers for a given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    # Global variable declaration of the Reddit api
    REDDIT_API = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)

    # Request
    req = requests.get(REDDIT_API, headers={
        'User-Agent': '0x16-api_advanced:project: v1.0.0 (by /u/kinyarasam)'
        }).json()

    # Get subs.
    subs = req.get("data", {}).get("subscribers", 0)
    return subs

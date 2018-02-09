"""
The application code needed to run BuddyBot.
"""
import collections
import praw
from .crawler import Crawler

TARGET_SUBREDDITS = [
    'Automate',
    'AwesomeBots',
    'AInotHuman',

]

LARGE_SUBREDDITS = [
    'worldnews',
    'funny',
    'pics',
    'jokes',
    'sports',
    'askreddit',
    'videos',
    'todayilearned',
    'gaming',
    'movies',
    'news',
    'gifs',
    'mildlyinteresting',
    'aww',
    'Showerthoughts',
    'television',
    'science',
    'OldSchoolCool',
    'IAmA',
    'Documentaries',
    'explainlikeimfive',
]

# Needed for anti-abuse functions
SUBMISSION_COUNT = collections.Counter()

def main():
    """
    The main function of the BuddyBot application.
    """
    # [WARN] Make sure to gitignore praw.ini! [WARN]
    reddit = praw.Reddit('BUDDYBOT', user_agent='BuddyBot_User_Agent')
    # For testing
    reddit.read_only = True

    for subreddit in LARGE_SUBREDDITS:
        crawler = Crawler(subreddit=subreddit, submission_limit=100, ignore_case=True)
        crawler.crawl_subreddit()

if __name__ == '__main__':
    main()

"""
The application code needed to run BuddyBot.
"""
import collections
import praw
from buddybot import Crawler

TARGET_SUBREDDITS = [
    'Automate',
    'AwesomeBots',
    'AInotHuman',

]

LARGE_SUBREDDITS = [
    'funny',
    'pics',
    'jokes',
    'sports',
    'askreddit',
    'videos',
    'gaming',
    'movies',
    'gifs',
    'mildlyinteresting',
    'aww',
    'Showerthoughts',
    'television',
    'OldSchoolCool',
    'IAmA',
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
        crawler = Crawler(subreddit=reddit.subreddit(subreddit),
                          sub_proc_limit=100,
                          comment_proc_limit=10000,
                          ignore_case=True)
        # TODO Add logging
        print("Processing /r/{subreddit}".format(subreddit=subreddit))
        crawler.crawl_subreddit()

if __name__ == '__main__':
    main()

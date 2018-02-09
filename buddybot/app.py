"""
The application code needed to run BuddyBot.
"""
import collections
import praw

TARGET_SUBREDDITS = [
    'Automate',
    'AwesomeBots',
    'AInotHuman',

]

# Needed for anti-abuse functions
SUBMISSION_COUNT = collections.Counter()

def main():
    """
    The main function of the BuddyBot application.
    """
    # [WARN] Make sure to gitignore praw.ini! [WARN]
    reddit = praw.Reddit('BUDDYBOT', user_agent='BuddyBot_User_Agent')

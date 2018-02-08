"""
The application code needed to run BuddyBot.
"""
import praw

TARGET_SUBREDDITS = [
    'Automate',
    'AwesomeBots',
    'AInotHuman',

]

# [WARN] Make sure to gitignore praw.ini! [WARN]
# Keep bot config settings in praw.ini file
reddit = praw.Reddit('BUDDYBOT', user_agent='BuddyBot User Agent')

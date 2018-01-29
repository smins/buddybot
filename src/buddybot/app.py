"""
The application code needed to run BuddyBot.
"""
import praw

# Keep bot config settings in praw.ini file - [WARN] Make sure to gitignore praw.ini! [WARN]
reddit = praw.Reddit('buddybot')

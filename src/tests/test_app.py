"""
Test suite for BuddyBot app.py
"""
import praw

class TestApp(object):
    """
    Test class for general BuddyBot app / praw operations
    """
    test_reddit_ini = praw.Reddit('buddybot')

    def test_construct_from_ini(self):
        """
        Tests that a reddit instance can be created using the praw.ini pattern
        """
        assert isinstance(self.test_reddit_ini, praw.Reddit)

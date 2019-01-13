"""
Test suite for crawler.py
"""

from buddybot import Crawler

class TestCrawler(object):
    """
    Tests BuddyBot3000 Crawlers
    """
    test_subreddit = 'BuddyBot'

    crawler = Crawler(subreddit=test_subreddit,
                      thread_proc_limit=100,
                      comment_proc_limit=1000,
                      ignore_case=True)

    def test_construct(self):
        """
        Tests that Crawlers can be constructed
        """
        assert isinstance(self.crawler, Crawler)

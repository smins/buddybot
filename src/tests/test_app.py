"""
Test suite for BuddyBot app.py.
"""

import random
from buddybot import FRIEND_TERMS
from buddybot import VALID_OPENER
from buddybot.app import Retort

class TestRetort(object):
    """
    Test class for a BuddyBot Retort
    """

    # Pick a random mirror_term, don't set second_term
    mirror_term = str(random.sample(FRIEND_TERMS, 1))
    retort = Retort(opener=VALID_OPENER, mirror_term=mirror_term)

    def test_opener(self):
        """
        Tests that the generated retort has a valid opener
        """
        assert VALID_OPENER in self.retort.formatted()

    def test_retort_mirror_term(self):
        """
        Tests that the generated retort has a valid first friend term - the mirrored term.

        The 'mirror term' should be the second friend term of the post you are responding to, e.g.:
            I'm not your buddy, pal.
            I'm not your pal, friend.
        """

        assert self.mirror_term in self.retort.formatted()

    def test_retort_second_term_random(self):
        """
        Tests that the generated retort has a valid second term when it set randomly.
        """
        assert any([term in self.retort.formatted() for term in FRIEND_TERMS])

    def test_retort_second_term_chosen(self):
        """
        Tests that the generated retort has a valid second term when it is set explicitly.
        """
        self.retort.second_term = 'friendo'
        assert 'friendo' in self.retort.formatted()

        self.retort.second_term = 'pal'
        assert 'pal' in self.retort.formatted()

class TestSplitter(object):
    """
    Test class for a BuddyBot Splitter
    """
    pass

class TestDetector(object):
    """
    Test class for a BuddyBot Detector
    """
    pass

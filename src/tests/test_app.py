"""
Test suite for BuddyBot app.py.
"""

import random
from buddybot import JOKE_PRINT_TEMPLATE
from buddybot import JOKE_REGEX_TEMPLATE
from buddybot import FRIEND_TERMS
from buddybot import VALID_OPENERS
from buddybot.app import Crawler
from buddybot.app import Retort

class TestCrawler(object):
    """
    Test class for a BuddyBot Crawler
    """

    # Pick a random opener, then pick random mirror_term and second_term,
    # different from each other.
    opener = str(random.sample(VALID_OPENERS, 1)[0])
    mirror_term, second_term = random.sample(FRIEND_TERMS, 2)

    crawler = Crawler(valid_openers=VALID_OPENERS,
                      regex_template=JOKE_REGEX_TEMPLATE)

    def test_detect_allopeners(self):
        """
        Test that a Crawler can detect instances of The Joke with any valid opener.
        """
        for opener in VALID_OPENERS:
            joke_string = JOKE_PRINT_TEMPLATE.format(opener=opener,
                                                     mirror_term=self.mirror_term,
                                                     second_term=self.second_term)
            assert self.crawler.detect_joke(joke_string)

    def test_detect_trueneg(self):
        """
        Test that a Crawler correctly ignores non-Joke strings.
        """
        test_strings = [
            "Hi I'm BuddyBot",
            "Do you wan't to be my friend?",
            "I like waffles."
        ]

        for test_str in test_strings:
            assert self.crawler.detect_joke(test_str) is False

    def test_split_allopeners(self):
        """
        Test that a Crawler can split instances of The Joke with any valid opener
        """
        pass

class TestRetort(object):
    """
    Test class for a BuddyBot Retort
    """

    # Pick a random opener, then pick random mirror_term and second_term, different from each other.
    opener = str(random.sample(VALID_OPENERS, 1)[0])
    mirror_term, second_term = random.sample(FRIEND_TERMS, 2)

    # Create Retort objects with & without optional second_term param set
    retort_noparam = Retort(mirror_term=mirror_term, opener=opener)
    retort_param = Retort(mirror_term=mirror_term,
                          opener=opener,
                          second_term=second_term)

    # Correctly formatted Joke using the randomly selected params
    test_formatted = JOKE_PRINT_TEMPLATE.format(opener=opener,
                                                mirror_term=mirror_term,
                                                second_term=second_term)

    def test_retort_constructor_noparam(self):
        """
        Tests that an object of type Retort can be created without optional parameters
        """
        assert isinstance(self.retort_noparam, Retort)

    def test_retort_constructor_params(self):
        """
        Tests that an object of type Retort can be created with optional parameters
        """
        assert isinstance(self.retort_param, Retort)

    def test_retort_mirror_term(self):
        """
        Tests that the generated retorts have a valid mirrored term
        """
        assert self.mirror_term in self.retort_noparam.formatted()
        assert self.mirror_term in self.retort_param.formatted()

    def test_retort_second_term_param(self):
        """
        Tests that the generated retort has a valid second term when it is set explicitly.
        """
        assert self.second_term in self.retort_param.formatted()

    def test_retort_second_term_random(self):
        """
        Tests that the generated retort has a valid second term when it set randomly.
        """
        assert any([term in self.retort_noparam.formatted() for term in FRIEND_TERMS])

    def test_retort_formatted_param(self):
        """
        Tests that the generated retort has a valid formatted() output
        """
        assert self.test_formatted == self.retort_param.formatted()

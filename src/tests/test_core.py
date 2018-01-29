"""
Test suite for BuddyBot core.py
"""

import random
from buddybot import SUMMON_KEYWORDS
from buddybot import JOKE_PRINT_TEMPLATE
from buddybot import JOKE_REGEX_TEMPLATE
from buddybot import FRIEND_TERMS
from buddybot import VALID_OPENERS
from buddybot.core import Crawler
from buddybot.core import Retort

class TestCrawler(object):
    """
    Test class for a BuddyBot Crawler
    """

    # Pick a random opener, then pick random mirror_term and second_term,
    # different from each other.
    opener = str(random.sample(VALID_OPENERS, 1)[0])
    first_term, second_term = random.sample(FRIEND_TERMS, 2)

    test_joke = JOKE_PRINT_TEMPLATE.format(opener=opener,
                                           mirror_term=first_term,
                                           second_term=second_term)

    test_nonjokes = [
        "Hi I'm BuddyBot",
        "Do you wan't to be my friend?",
        "I like waffles."
    ]

    test_nonsummon = [
        "!Buddy",
        "!Wikibot",
        "!",
        "BuddyBot",
        "BuddyBot3000"
    ]

    crawler_noparam = Crawler(summon_kws=SUMMON_KEYWORDS, valid_openers=VALID_OPENERS)
    crawler_params = Crawler(summon_kws=SUMMON_KEYWORDS,
                             valid_openers=VALID_OPENERS,
                             regex_template=JOKE_REGEX_TEMPLATE)

    def test_crawler_construct_noparam(self):
        """
        Tests that an object of type Crawler can be created without optional parameters
        """
        assert isinstance(self.crawler_noparam, Crawler)

    def test_crawler_construct_params(self):
        """
        Tests that an object of type Crawler can be created with optional parameters
        """
        assert isinstance(self.crawler_params, Crawler)

    def test_crawler_detect_allopeners(self):
        """
        Test that a Crawler can detect instances of The Joke with any valid opener.
        """
        for opener in VALID_OPENERS:
            joke_string = JOKE_PRINT_TEMPLATE.format(opener=opener,
                                                     mirror_term=self.first_term,
                                                     second_term=self.second_term)
            assert self.crawler_params.detect_joke(joke_string)

    def test_crawler_detect_trueneg(self):
        """
        Test that a Crawler correctly ignores non-Joke strings.
        """
        for test_str in self.test_nonjokes:
            assert self.crawler_params.detect_joke(test_str) is False

    def test_crawler_detect_allsummons(self):
        """
        Test that a Crawler correctly detects its summon_keywords.
        """
        for summon_kw in SUMMON_KEYWORDS:
            assert self.crawler_params.detect_summons(summon_kw)

    def test_crawler_detect_negsummons(self):
        """
        Test that a Crawler ignores non-summon keywords
        """
        for non_key in self.test_nonsummon:
            assert self.crawler_params.detect_summons(non_key) is False

    def test_crawler_create_joke(self):
        """
        Test that a crawler succesfully generates a random instance of the Joke.

        Dependent on the test_crawler_detect_allopeners test passing
        """
        random_retort = self.crawler_params.gen_random_retort()
        assert self.crawler_params.detect_joke(random_retort.formatted())

    def test_crawler_split_opener(self):
        """
        Test that a Crawler can correctly split openers from Joke instances
        """
        assert self.opener == self.crawler_params.split_joke(self.test_joke)[0]

    def test_crawler_split_first_term(self):
        """
        Test that a Crawler can split the first friend_term from Joke instances
        """
        assert self.first_term == self.crawler_params.split_joke(self.test_joke)[1]

    def test_crawler_split_second_term(self):
        """
        Test that a Crawler can split the second friend_term from Joke instances
        """
        assert self.second_term == self.crawler_params.split_joke(self.test_joke)[2]

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

    def test_retort_construct_noparam(self):
        """
        Tests that an object of type Retort can be created without optional parameters
        """
        assert isinstance(self.retort_noparam, Retort)

    def test_retort_construct_params(self):
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

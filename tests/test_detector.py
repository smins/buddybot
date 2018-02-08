"""
Test suite for detector.py
"""

from buddybot import Detector

class TestDetector(object):
    """
    Test class for a BuddyBot Detector
    """
    # Define some valid and invalid jokes
    test_jokes = [
        "I'm not your buddy, friend.",
        "I'm not your boiii, fam.",
        "I'm not your mate, pal"
    ]
    test_jokes_lower = [
        "i'm not your buddy, friend.",
        "i'm not your boiii, fam",
        "i'm not your mate, pal"
    ]
    test_nonjokes = [
        "Hi I'm BuddyBot",
        "Do you wan't to be my friend?",
        "I like waffles."
    ]

    # Define some valid and invalid summons
    test_summons = [
        '!BuddyBot3000',
        '!BuddyBot'
    ]
    test_summons_lower = [
        '!buddybot3000',
        '!buddybot'
    ]
    test_nonsummons = [
        "!Buddy",
        "!Wikibot",
        "!",
        "BuddyBot",
        "BuddyBot3000"
    ]

    detector = Detector()
    cased_detector = Detector(ignore_case=False)

    def test_base_construct(self):
        """
        Tests that an object of type Detector can be created without parameters.
        """
        assert isinstance(self.detector, Detector)

    def test_cased_construct(self):
        """
        Tests that an object of type Detector can be created with ignore_case param.
        """
        assert isinstance(self.cased_detector, Detector)

    def test_base_detect_joke_upper(self):
        """
        Test that a base detector correctly detects correctly cased jokes.
        """
        for test_joke in self.test_jokes:
            assert self.detector.detect_joke(test_joke) is True

    def test_base_detect_joke_lower(self):
        """
        Test that a base detector correctly detects correctly cased jokes.
        """
        for test_joke in self.test_jokes_lower:
            assert self.detector.detect_joke(test_joke) is True

    def test_cased_detect_joke_upper(self):
        """
        Test that a cased detector correctly detects correctly cased jokes.
        """
        for test_joke in self.test_jokes:
            assert self.cased_detector.detect_joke(test_joke) is True

    def test_cased_ignore_joke_lower(self):
        """
        Test that a cased detector correctly ignores lowercase joke strings
        """
        for test_joke in self.test_jokes_lower:
            assert self.cased_detector.detect_joke(test_joke) is False

    def test_ignore_nonjoke(self):
        """
        Test that both base and cased detectors correctly ignore non-Joke strings.
        """
        for test_nonjoke in self.test_nonjokes:
            assert self.detector.detect_joke(test_nonjoke) is False
            assert self.cased_detector.detect_joke(test_nonjoke) is False

    def test_base_detect_summons_upper(self):
        """
        Test that a base detector correctly detects uppercase summon_keywords.
        """
        for summon_kw in self.test_summons:
            assert self.detector.detect_summon(summon_kw) is True

    def test_base_detect_summons_lower(self):
        """
        Test that a base detector correctly detects lowercase summon_keywords.
        """
        for summon_kw in self.test_summons_lower:
            assert self.detector.detect_summon(summon_kw) is True

    def test_cased_detect_summons_upper(self):
        """
        Test that a cased detector correctly detects uppercase summon_keywords.
        """
        for summon_kw in self.test_summons:
            assert self.cased_detector.detect_summon(summon_kw) is True

    def test_cased_ignore_summons_lower(self):
        """
        Test that a base detector correctly ignores lowercase summon_keywords.
        """
        for summon_kw in self.test_summons_lower:
            assert self.cased_detector.detect_summon(summon_kw) is False

    def test_ignore_nonsummons(self):
        """
        Test that both base and cased detectors ignore non-summon keywords.
        """
        for non_kw in self.test_nonsummons:
            assert self.detector.detect_summon(non_kw) is False
            assert self.cased_detector.detect_summon(non_kw) is False

    def test_get_last_match(self):
        """
        Test that a detector can return its last match as a string.
        """
        test_match = "I'm not your buddy, pal."
        self.detector.detect_joke(test_match)
        assert self.detector.get_last_match() == test_match

    def test_get_last_match_comps(self):
        """
        Test that a detector can return its last match as its three components.
        """
        test_match = "I'm not your buddy, pal."
        test_comps = ("I'm not your", "buddy", "pal")

        self.detector.detect_joke(test_match)
        comps = self.detector.get_last_match_comps()
        assert comps == test_comps

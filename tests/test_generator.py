"""
Test suite for jokegenerator.py
"""

from buddybot import Detector
from buddybot import JokeGenerator

class TestGenerator(object):
    """
    Tests BuddyBot3000 JokeGenerators
    """

    detector = Detector()
    generator = JokeGenerator()

    def test_random_joke(self):
        """
        Use a Detector to test that a JokeGenerator can create a valid random retort

        Dependent on test_detector.py
        """
        random_joke_str = self.generator.get_random_joke().get_str()
        assert self.detector.detect_joke(random_joke_str)

    def test_reponse_joke(self):
        """
        Test that a JokeGenerator can create a proper response from components.

        Dependent on test_random_retort
        Dependent on test_detector.py
        """
        # Create a random response and extract its components
        random_joke_str = self.generator.get_random_joke().get_str()
        self.detector.detect_joke(random_joke_str)

        comps_orig = self.detector.get_last_match_comps()

        # Create the response and check that it a valid retort
        response_str = self.generator.get_response_joke(comps_orig).get_str()
        assert self.detector.detect_joke(response_str)

        comps_new = self.detector.get_last_match_comps()
        assert all([
            comps_orig[0] == comps_new[0],
            comps_orig[2] == comps_new[1]
            ])

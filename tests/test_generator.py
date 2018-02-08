"""
Test suite for generator.py
"""

from buddybot import Detector, Generator

class TestGenerator(object):
    """
    Tests BuddyBot3000 Generators
    """

    detector = Detector()
    generator = Generator()

    def test_random_retort(self):
        """
        Use a Detector to test that a Generator can create a valid random retort

        Dependent on test_detector.py
        """
        random_retort = self.generator.get_random()
        assert self.detector.detect_joke(random_retort)

    def test_reponse(self):
        """
        Test that a Generator can create a proper response from components.

        Dependent on test_random_retort
        Dependent on test_detector.py
        """
        # Create a random response and extract its components
        random_retort = self.generator.get_random()
        self.detector.detect_joke(random_retort)
        comps = self.detector.get_last_match_comps()

        # Create the response and check that it a valid retort
        response = self.generator.get_response(comps)
        assert self.detector.detect_joke(response)

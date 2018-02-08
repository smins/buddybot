"""
BuddyBot Detector
"""
import re
import buddybot

class Detector(object):
    """
    Detects valid instances of The Joke or the summons keywords.
    Tracks its last match and its components.
    """
    def __init__(self, ignore_case=True):

        self.ignore_case = ignore_case

        # Capture groups allow extraction of joke components
        self.joke_regex = r"({opener}) ([a-zA-Z]+), ([a-zA-Z]+)."
        self.valid_openers = buddybot.VALID_OPENERS

        self.summon_kws = [
            '!BuddyBot3000',
            '!BuddyBot'
            ]

        self.last_match = None
        self.last_match_components = None

    def _get_re_flags(self):
        """
        Returns a list of flags, handling the ignore_case param
        """
        if self.ignore_case:
            return re.IGNORECASE

        # Default value of re.compile flags
        return 0

    def detect_joke(self, target_str):
        """
        Detects instances of The Joke.
        """
        flags = self._get_re_flags()
        for opener in self.valid_openers:
            pattern = re.compile(self.joke_regex.format(opener=opener), flags=flags)
            match = re.match(pattern, target_str)
            if match:
                self.last_match = match.group(0)
                self.last_match_components = match.group(1, 2, 3)

                return True

        return False

    def detect_summon(self, target_str):
        """
        Detects exact matches of the summon keywords.
        """
        flags = self._get_re_flags()
        for summon_kw in self.summon_kws:
            pattern = re.compile(summon_kw, flags=flags)
            if re.match(pattern, target_str):
                return True

        return False

    def get_last_match(self):
        """
        Returns the last matched joke as a string.
        """
        return self.last_match

    def get_last_match_comps(self):
        """
        Returns the last match as a tuple of it's components:
        (opener, first_term, second_term)
        """
        return self.last_match_components

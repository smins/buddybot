"""
The core BuddyBot Mk 3000 application code.
"""

import random
import re
from buddybot import JOKE_REGEX_TEMPLATE
from buddybot import JOKE_PRINT_TEMPLATE
from buddybot import FRIEND_TERMS

class Crawler(object):
    """
    Detects valid instances of The Joke and splits them into components
    """
    def __init__(self, valid_openers, regex_template=JOKE_REGEX_TEMPLATE):
        self.valid_openers = valid_openers
        self.regex_template = regex_template

    def _match_template(self, target_str):
        """
        Detects instances of The Joke, returns their three components. Returns None on no-match.

        Components:
        opener: How the joke begins, typically "I'm not your"
        first_term: The first 'friend term' (e.g. buddy, pal, etc.) of the instance being split.
        second_term: The second term of a Joke instance, repeated in a Retort as the first term.
        """
        for opener in self.valid_openers:
            # Ignore case during matching
            pattern = re.compile(self.regex_template.format(opener=opener), flags=re.IGNORECASE)
            match = re.match(pattern, target_str)
            if match:
                return match.group(1, 2, 3)

        return None

    def detect_joke(self, target_str):
        """
        Returns a bool indicating if a target_str is an instance of The Joke

        Wrapper around _match_template
        """
        return bool(self._match_template(target_str=target_str))

    def split_joke(self, joke_str):
        """
        Returns the three components of a given instance of The Joke.

        Wrapper around _match_template
        """
        return self._match_template(joke_str)

class Retort(object):
    """
    A BuddyBot's Retort to the outrageous statement that a user is its buddy, pal, or friend.
    """

    def __init__(self, opener, mirror_term, second_term=None, template=JOKE_PRINT_TEMPLATE):
        # Opener must be the same as parent comment to properly continue The Joke
        self.opener = opener
        # The first term (mirror_term) must be the parent comment's second_term to continue The Joke
        self.mirror_term = mirror_term
        # Templates must have keywords 'opener', 'mirror_term', and 'second_term'
        self.template = template

        if second_term is None:
            self.second_term = str(random.sample(FRIEND_TERMS, 1))
        else:
            self.second_term = second_term

    def get_components(self):
        """
        Returns the opener, mirror_term, and second_term of this Retort as a tuple
        """

        return self.opener, self.mirror_term, self.second_term

    def formatted(self):
        """
        Returns a formatted string of this Retort
        """

        return self.template.format(opener=self.opener,
                                    mirror_term=self.mirror_term,
                                    second_term=self.second_term)

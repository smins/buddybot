"""
The core BuddyBot Mk 3000 application code.

All instances of The Joke are referring to the "I'm not your {buddy}, {pal}" meme
See: https://www.urbandictionary.com/define.php?term=I%27m%20not%20your%20friend%2C%20buddy
"""

import random
from buddybot import FRIEND_TERMS


class Detector(object):
    """
    Detects valid instances of The Joke.
    """
    def __init__(self):
        pass

class Splitter(object):
    """
    Splits instances of The Joke into their components: opener, first term, and second term.

    opener: Typically "I'm not your ". Variations such as "Don't call me " exist.
    first_term: The first 'friend term' (e.g. buddy, pal, etc.) of the instance being split.
    second_term: The second friend term of a Joke instance, must be repeated in a Retort to it.
    """

    def __init__(self, joke_str):
        self.joke_str = joke_str

class Retort(object):
    """
    A BuddyBot's Retort to the outrageous statement that a user is its buddy, pal, or friend.
    """

    def __init__(self, opener, mirror_term, second_term=None):
        self.opener = opener
        self.mirror_term = mirror_term
        if second_term is None:
            self.second_term = random.sample(FRIEND_TERMS, 1)
        else:
            self.second_term = second_term

    def formatted(self):
        """
        Returns a formatted string of this Retort
        """
        return '{opener}{mirrored_term}{random_term}'.format(opener=self.opener,
                                                             mirrored_term=self.mirror_term,
                                                             random_term=self.second_term)

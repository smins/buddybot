"""
The core BuddyBot Mk 3000 application code.

All instances of The Joke are referring to the "I'm not your {buddy}, {pal}" meme from South Park
See:
https://www.urbandictionary.com/define.php?term=I%27m%20not%20your%20friend%2C%20buddy
http://southpark.cc.com/clips/165191/im-not-your-friend-guy
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

    def detect_joke(self, target_str):
        """
        Detects instances of The Joke that match the template and use valid openers

        Casts both the target & the valid openers to lowercase during the check
        """
        for opener in self.valid_openers:
            cast_template = self.regex_template.format(opener=opener.lower())
            if re.match(cast_template, target_str.lower()):
                return True

        return False

    def split_joke(self, joke_str):
        """
        Splits known instances of The Joke into the template: opener, first term, and second term.

        opener: How the joke begins, typically "I'm not your"
        first_term: The first 'friend term' (e.g. buddy, pal, etc.) of the instance being split.
        second_term: The second term of a Joke instance, repeated in a Retort as the first term.
        """
        pass

class Retort(object):
    """
    A BuddyBot's Retort to the outrageous statement that a user is its buddy, pal, or friend.
    """

    def __init__(self, opener, mirror_term, second_term=None, template=JOKE_PRINT_TEMPLATE):
        # Opener must be the same as parent comment to properly continue The Joke
        self.opener = opener
        self.mirror_term = mirror_term
        # Templates must have keywords 'opener', 'mirror_term', and 'second_term'
        self.template = template

        if second_term is None:
            self.second_term = str(random.sample(FRIEND_TERMS, 1))
        else:
            self.second_term = second_term

    def formatted(self):
        """
        Returns a formatted string of this Retort
        """

        return self.template.format(opener=self.opener,
                                    mirror_term=self.mirror_term,
                                    second_term=self.second_term)

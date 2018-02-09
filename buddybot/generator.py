"""
BuddyBot Joke Generator
"""
import random
from .joke import Joke, FRIEND_TERMS, VALID_OPENERS

class JokeGenerator(object):
    """
    Generates retorts to the preposterous statement that a user is its buddy, pal, or friend.
    """
    def __init__(self):
        self.template = "{opener} {first_term}, {second_term}."

    def get_response_joke(self, components):
        """
        Returns a Joke created from the passed joke components.
        (opener, first_term, second_term)
        """
        # Drop the passed first_term & randomly sample a new second_term
        opener, _, second_term = components
        new_second_term = str(random.sample(FRIEND_TERMS, 1)[0])

        # Mirror the opener & place the passed second_term as the first_term
        return Joke(opener=opener,
                    first_term=second_term,
                    second_term=new_second_term)

    def get_random_joke(self):
        """
        Returns a randomly generated Joke when summoned by a user.
        """
        opener = str(random.sample(VALID_OPENERS, 1)[0])
        first_term, second_term = random.sample(FRIEND_TERMS, 2)

        return Joke(opener=opener, first_term=first_term, second_term=second_term)

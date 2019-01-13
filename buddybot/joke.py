"""
Defines the Joke class and constants
"""

VALID_OPENERS = [
    "I'm not your",
    "Don't call me"
]

FRIEND_TERMS = [
    'acquaintance',
    'associate',
    'boss',
    'boiii'
    'bro',
    'brother',
    'buddy',
    'captain',
    'champ',
    'chief',
    'chum',
    'coach',
    'companion',
    'compatriot',
    'comrade',
    'consort',
    'cousin',
    'daddy',
    'deputy',
    'fam',
    'friend',
    'friendo',
    'mate',
    'pal',
    'partner',
    'peon',
    'ref',
    'sidekick',
    'sister',
    'soulmate',
    'squad',
    'temp',
    'queen'
]

class Joke(object):
    """
    A NotYourBuddy form Joke.
    """

    def __init__(self, opener, first_term, second_term):
        self.opener = opener
        self.first_term = first_term
        self.second_term = second_term

        self.template = r"{opener} {first_term}, {second_term}."

    def __str__(self):
        return self.template.format(opener=self.opener,
                                    first_term=self.first_term,
                                    second_term=self.second_term)

    def get_template(self):
        """
        Returns this joke's template.
        """
        return self.template

    def get_str(self):
        """
        Returns the string form of the joke
        """
        return self.template.format(opener=self.opener,
                                    first_term=self.first_term,
                                    second_term=self.second_term)

    def get_comps(self):
        """
        Returns the components of the joke as a tuple
        """
        return self.opener, self.first_term, self.second_term

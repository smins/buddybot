"""
Constants that define The Joke
See: https://www.urbandictionary.com/define.php?term=I%27m%20not%20your%20friend%2C%20buddy
"""

# Templates to detect & print The Joke
# Use raw strings for regex
JOKE_REGEX_TEMPLATE = r"{opener} [a-z]+, [a-z]+."
JOKE_PRINT_TEMPLATE = "{opener} {mirror_term}, {second_term}."

# Support "Don't call me " variant
VALID_OPENERS = [
    "I'm not your",
    "Don't call me"
]

# Mostly sourced from http://www.thesaurus.com
FRIEND_TERMS = [
    'acquaintance',
    'associate',
    'bro',
    'brother',
    'buddy',
    'chum',
    'coach',
    'companion',
    'compatriot',
    'comrade',
    'consort',
    'cousin',
    'deputy',
    'friend',
    'friendo',
    'mate',
    'pal',
    'partner',
    'peon',
    'ref',
    'sidekick',
    'soulmate',
    'temp'
]

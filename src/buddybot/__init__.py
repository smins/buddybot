"""
All instances of The Joke are referring to the "I'm not your {buddy}, {pal}" meme from South Park
See:

https://www.urbandictionary.com/define.php?term=I%27m%20not%20your%20friend%2C%20buddy
http://southpark.cc.com/clips/165191/im-not-your-friend-guy

Set constants that define The Joke
"""

TARGET_SUBREDDITS = [
    'Automate',
    'AwesomeBots',
    'AInotHuman',

]

SUMMON_KEYWORDS = [
    '!BuddyBot3000',
    '!BuddyBot'
]

# Templates to detect & print The Joke
# Use raw strings for regex
JOKE_REGEX_TEMPLATE = r"({opener}) ([a-zA-Z]+), ([a-zA-Z]+)."
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
    'boss',
    'boiii'
    'bro',
    'brother',
    'buddy',
    'champ',
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

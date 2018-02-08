"""
BuddyBot Mk 3000

All instances of The Joke are referring to the "I'm not your {buddy}, {pal}" meme from South Park
http://southpark.cc.com/clips/165191/im-not-your-friend-guy
"""

from .crawler import Crawler
from .detector import Detector
from .generator import Generator

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

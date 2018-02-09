"""
BuddyBot Mk 3000

All instances of The Joke are referring to the "I'm not your {buddy}, {pal}" meme from South Park
http://southpark.cc.com/clips/165191/im-not-your-friend-guy
"""
from .crawler import Crawler
from .detector import Detector
from .joke import Joke, VALID_OPENERS, FRIEND_TERMS
from .generator import JokeGenerator

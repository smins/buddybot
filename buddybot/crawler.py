"""
BuddyBot Crawler
"""
import praw
from .detector import Detector
from .generator import JokeGenerator

class Crawler(object):
    """
    Crawlers wrap processing logic around the input source - a subreddit in this case
    """
    def __init__(self, subreddit, submission_limit=100, ignore_case=True):

        # A praw reddit.subreddit
        self.subreddit = subreddit
        self.submission_limit = submission_limit
        self.ignore_case = ignore_case

        self.detector = Detector(ignore_case=self.ignore_case)
        self.generator = JokeGenerator()

        # generator that yields new threads
        self._submission_gen = self._create_sub_generator()

    def _create_sub_generator(self):
        """
        Returns a generator that yields the next submission in this subreddit's stream.
        After dispensing thread_limit submissions, it will yield None
        """
        outputs = 0
        while outputs < self.submission_limit:
            try:
                yield next(self.subreddit.stream.submissions())
                outputs += 1
            except StopIteration:
                yield None
                break

        yield None

    def crawl_subreddit(self):
        """
        Process the subreddit this Crawler was constructed with.
        """
        submission = next(self._submission_gen)
        while submission is not None:
            self.crawl_submission(submission)


    def crawl_submission(self, submission):
        """
        Expand the comment trees of a praw submission, then process its comments.
        """

        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            self.process_comment(comment)

    def process_comment(self, comment):
        """
        Determines if the body of a praw comment is a summon or Joke, and replies accordingly.
        """

        if self.detector.detect_summon(comment.body):
            reply = self.generator.get_random_joke()

        elif self.detector.detect_joke(comment.body):
            joke_comps = self.detector.get_last_match_comps()
            reply = self.generator.get_response_joke(components=joke_comps)

        # TODO Post reply using anti-abuse functions
        print("Comment: {comment} \n Reply: {reply}".format(comment=comment, reply=reply))

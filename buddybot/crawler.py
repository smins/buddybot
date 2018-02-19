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
    def __init__(self, subreddit, sub_proc_limit=100, comment_proc_limit=None, ignore_case=True):

        # A praw reddit.subreddit
        self.subreddit = subreddit
        self.sub_proc_limit = sub_proc_limit
        self.comment_proc_limit = comment_proc_limit
        self.ignore_case = ignore_case

        self.detector = Detector(ignore_case=self.ignore_case)
        self.generator = JokeGenerator()

        # generator that yields new threads
        self._sub_gen = self._create_sub_generator()

    def _create_sub_generator(self):
        """
        Returns a generator that yields submissions from the 'hot' list of the crawler's subreddit

        Used in the constructor
        """
        for sub in self.subreddit.hot(limit=self.sub_proc_limit):
            yield sub

        return

    def crawl_subreddit(self):
        """
        Crawlers the subreddit this Crawler was constructed
        """

        subs_procd = 0
        try:
            # Grab the next submission from the generator
            target_submission = next(self._sub_gen)
            while target_submission is not None:
                self.process_submission(target_submission)

                subs_procd += 1
                if subs_procd % 10 == 0:
                    print(target_submission.title)
                    print("Subs processed: {0}".format(subs_procd))

                target_submission = next(self._sub_gen)

        except StopIteration:
            # Reached thread limit for this test_subreddit, so move on
            return

    def process_submission(self, submission):
        """
        Iterativelly process the comments of a praw submission
        """

        comments_procd = 0
        # Expand the comment forest up to the comment_proc_limit
        submission.comments.replace_more(limit=self.comment_proc_limit)
        for comment in submission.comments.list():
            comments_procd += 1
            self.process_comment(comment)

            comments_procd += 1
            if comments_procd % 100 == 0:
                print(comment.body)
                print("Comments processed: {0}".format(comments_procd))

    def process_comment(self, comment):
        """
        Determines if the body of a praw comment is a summon or Joke, and replies accordingly.
        """

        # TODO: Add logging
        # TODO: Add anti-abuse submission

        if self.detector.detect_summon(comment.body):
            bb_response = self.generator.get_random_joke().get_str()
            print("Comment: {comment} \n Reply: {reply}".format(comment=comment.body,
                                                                reply=bb_response))

        elif self.detector.detect_joke(comment.body):
            joke_comps = self.detector.get_last_match_comps()
            bb_response = self.generator.get_response_joke(components=joke_comps).get_str()
            print("Comment: {comment} \n Reply: {reply}".format(comment=comment.body,
                                                                reply=bb_response))

        return

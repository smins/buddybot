"""
BuddyBot Crawler
"""
import praw
from .detector import Detector
from .generator import JokeGenerator

class Crawler(object):
    """
    Crawlers wrap processing logic around the input source - a subreddit
    """
    def __init__(self, subreddit, thread_proc_limit=100, comment_proc_limit=None, ignore_case=True):

        # A praw reddit.subreddit
        self.subreddit = subreddit
        self.thread_proc_limit = thread_proc_limit
        self.comment_proc_limit = comment_proc_limit
        self.ignore_case = ignore_case

        self.detector = Detector(ignore_case=self.ignore_case)
        self.generator = JokeGenerator()

        # generator that yields new threads
        self._thread_gen = self._create_thread_generator()

    def _create_thread_generator(self):
        """
        Returns a generator that yields submissions from the 'hot' list of the crawler's subreddit

        Used in the constructor
        """
        for thread in self.subreddit.hot(limit=self.thread_proc_limit):
            yield thread

        return

    def crawl_subreddit(self):
        """
        Crawlers the subreddit this Crawler was constructed
        """

        threads_procd = 0
        try:
            # Grab the next thread from the generator
            target_thread = next(self._thread_gen)
            while target_thread is not None:
                self.process_submission(target_thread)

                threads_procd += 1
                if threads_procd % 10 == 0:
                    print(target_thread.title)
                    print("Threads processed: {0}".format(threads_procd))

                target_thread = next(self._thread_gen)

        except StopIteration:
            # Reached thread limit for this subreddit, so move on
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
            # TODO: Remove Testing output
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
            print("******************")
            print("Comment: {comment} \n Reply: {reply}".format(comment=comment.body,
                                                                reply=bb_response))
            print("******************")

        elif self.detector.detect_joke(comment.body):
            joke_comps = self.detector.get_last_match().get_comps()
            bb_response = self.generator.get_response_joke(components=joke_comps).get_str()
            print("******************")
            print("Comment: {comment} \n Reply: {reply}".format(comment=comment.body,
                                                                reply=bb_response))
            print("******************")

        return

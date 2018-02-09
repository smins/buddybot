import collections, praw

#Credit to acini@github.com for the original design and thanks for releasing this to public domain :)

#Note: comment_limit_reached resets on process restart

def is_summon_chain(reddit_instance, post):
    """
    Returns True if grandparent comment is bot's own
    Make sure to update the bot username
    """
    if not post.is_root:
        parent_comment_id = post.parent_id
        parent_comment = reddit_instance.get_info(thing_id=parent_comment_id)
        if parent_comment.author != None and str(parent_comment.author.name) == 'BuddyBot3000':
            return True

        return False

    return False

def comment_limit_reached(post, comment_limit=1):
    """
    Returns True if current will be greater than comment_limit in same thread.
    Resets on process restart
    """
    global SUBMISSION_COUNT
    count_of_this = int(float(submissioncount[str(post.submission.id)]))
    if count_of_this > comment_limit:
        return True
    else:
        return False

def is_already_done(post):
    done = False
    numofr = 0
    try:
        repliesarray = post.replies
        numofr = len(list(repliesarray))
    except:
        pass
    if numofr != 0:
        for repl in post.replies:
            if repl.author != None and repl.author.name == 'BuddyBot3000':
                done = True
                continue
    if done:
        return True
    else:
        return False

def post_reply(reply, post):
    global SUBMISSION_COUNT
    try:
        a = post.reply(reply)
        SUBMISSION_COUNT[str(post.submission.id)]+=1
        return True
    except Exception as e:
        warn("REPLY FAILED: %s @ %s"%(e,post.subreddit))
        if str(e) == '403 Client Error: Forbidden':
            print("/r/{subreddit} has banned me.".format(subreddit=post.subreddit))
            save_changing_variables()
    return False

SUBMISSION_COUNT = collections.Counter()

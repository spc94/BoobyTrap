import praw
import sys

reddit = praw.Reddit('bot2')


# If comment.author returns None, it means that our comment was successfully removed!
comment = reddit.comment(sys.argv[1])
if str(comment.author) == "None":
	print "This comment doesn't exist! (It was removed successfully)"
else:
	print "This comment still exists!"
import praw

reddit = praw.Reddit('bot2')

user = reddit.redditor('boobytrap_bot')

for reply in reddit.inbox.comment_replies():
	if "bad bot" in reply.body.lower():
		# Obtain the comment_id of the reply
		print reply.author
		print reply.body
		print reply.permalink
		comment_id = str(reply.permalink)[47:54]
		print comment_id

		# Generate the comment tree from the comment_id
		bad_comment = reddit.comment(comment_id)

		# Obtain our Bot's comment ID
		print bad_comment.parent().author
		print bad_comment.parent().id
		our_comment_id = bad_comment.parent().id

		# Generate our bot's comment object
		our_comment = reddit.comment(our_comment_id)

		# Deletes out bot's comment
		our_comment.delete()
		print "---------------"



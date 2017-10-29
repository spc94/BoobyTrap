import praw

reddit = praw.Reddit('bot2')

user = reddit.redditor('boobytrap_bot')

bad_comments_array = []

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

		# Saves bad comment info to an array if we haven't already deleted it.
		if str(bad_comment.parent().author) != "None":
			bad_comments_array.append(str(comment_id) + ", " + str(reply.author) + ", " + str(reply.body))
			print "COMMENT LOGGED"
		print "---------------"

with open("boobytrap_bad_comments.txt","a") as f:
		for comment in bad_comments_array:
			f.write(comment + "\n")



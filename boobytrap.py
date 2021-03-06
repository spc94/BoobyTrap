# -*- coding: utf-8 -*-
import praw
import sys
import pdb
import os
import re
import time
from random import randint
from praw.models import MoreComments

def saveArrays( comments_replied_to, submissions_opened ):
	with open("boobytrap_comments.txt","a") as f:
		for comment_id in comments_replied_to:
			f.write(comment_id + "\n")

	with open("boobytrap_submissions.txt","a") as f:
		for submission_id in submissions_opened:
			f.write(submission_id + "\n")

# Read and parse arguments
print str(sys.argv[1])

no_args 	   = len(sys.argv)
no_submissions = int(sys.argv[1]) 

if no_args != 2:
	print "You must include the number of submissions! \nEx: \"python boobytrap.py 300\" -> Searches through the Hottest 300 Submissions."
	sys.exit()
elif no_submissions < 1 or no_submissions > 1000:
	print "Use a number of submissions between 1 and 1000!"
	sys.exit()


reddit = praw.Reddit('bot2')

# Creates system files if not already created

# Checks or creates comments replied to file

if not os.path.isfile("boobytrap_comments.txt"):
	comments_replied_to = []
else:
	with open("boobytrap_comments.txt","r") as f:
		comments_replied_to = f.read()
		comments_replied_to = comments_replied_to.split("\n")
		comments_replied_to = list(filter(None, comments_replied_to))

# Checks or creates submissions opened file

if not os.path.isfile("boobytrap_submissions.txt"):
	submissions_opened = []
else:
	with open("boobytrap_submissions.txt","r") as f:
		submissions_opened = f.read()
		submissions_opened = submissions_opened.split("\n")
		submissions_opened = list(filter(None, submissions_opened))

subreddit = reddit.subreddit('all')
j=0
for i, submission in enumerate(subreddit.hot(limit=no_submissions)):

	if submission.id in submissions_opened:
		continue

	if j != 0 and j%25==0:
		print "Sleeping for 60 seconds"
		time.sleep(60)

	# Check if submission already opened
	if submission.id not in submissions_opened:
		for comment in submission.comments.list():

			# Ignores Load Null Authors (comments removed but ID still exists)
			try:
				comment.author.name
			except:
				continue

			flag = 0
			# Excludes comments already replied to and bot's own comments
			if (comment.id not in comments_replied_to) and (comment.author.name != "boobytrap_bot") and (comment.score > 10):
				if comment.body.lower().find("gallowboob") != -1:
					continue
				if comment.body.lower().find("boobs") != -1:
					try:
						comment.reply("[Here are some boobies, just for you!](https://i.imgur.com/5oX09ZZ.jpg)")
					except:
						print "Exception on Reply"
						continue
					flag = 1
				elif comment.body.lower().find("boobies") != -1:
					try:
						comment.reply("[Here are some boobies, just for you!](https://i.imgur.com/5oX09ZZ.jpg)")
					except:
						print "Exception on Reply"
						continue
					flag = 1
				elif comment.body.lower().find("boob") != -1:
					try:
						comment.reply("[Here's a boob, just for you!](https://i.imgur.com/Mf7awN4.jpg)")
					except:
						print "Exception on Reply"
						continue
					flag = 1
				elif comment.body.lower().find("tits") != -1:
					try:
						comment.reply("[Here are some great tits!](https://i.imgur.com/lNjL0e5.jpg)")
					except:
						print "Exception on Reply"
						continue
					flag = 1
				if flag == 1:
					comments_replied_to.append(comment.id)
					print "* COMMENT REPLIED TO *" 
	submissions_opened.append(submission.id)
	j = j+1
	print "* End of Submission *"

saveArrays(comments_replied_to, submissions_opened)


	# TODO
		# Find out where all the Null Authors are comming from
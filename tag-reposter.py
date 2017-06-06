#!/usr/bin/python

"""
A bot to repost content with a specific tag (e.g. [uk]) in the title to its own subreddit.
Built so I wouldn't have to sift through /r/roadcam for UK tagged content.
Runs as a cron job.
ads, June 2017.
"""

script_id=                                      # client id goes here
script_secret=                                  # client secret
uname =                                         # username for bot
pword =                                         # password
subreddit_title = "roadcam"                     # the subreddit to scan for posts
repost_subreddit = "ukdashcam"                  # the subreddit to repost them to
tagterm = '[uk]'                                # the tag term to search for

import praw,time

def main():
    r= praw.Reddit(client_id=script_id,client_secret=script_secret,password=pword,username=uname,user_agent="UK Dashcam repost script")

    for submission in r.subreddit(subreddit_title).new(limit=1000):
        if tagterm in submission.title.lower():
            try:
                print("Attempting to repost "+submission.title)
                r.subreddit(repost_subreddit).submit(submission.title,url=submission.url,send_replies=False,resubmit=False)

            except:
                print("Failed to repost"+submission.title)
                continue
        time.sleep(5)

main()
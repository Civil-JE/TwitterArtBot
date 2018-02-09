'''
Author: Josh Eastman
Updated: 02/08/2018
Description: Main file for Twitter Art Bot
'''
import praw
from createInstance import CreateRedditInstance

x = CreateRedditInstance()

GO = True



while(GO):
    x.setRedditInfo()

    #Don't need to provide user details to only needing a Read Only account.
    reddit = praw.Reddit(client_id=x.client_id, client_secret=x.client_secret, user_agent=x.user_agent)

    print(x.user_agent)
    for submission in reddit.subreddit('art').top(time_filter='week',limit=2):
        print(submission.title)
        print(submission.url)









      
    GO = False

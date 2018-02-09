'''
Author: Josh Eastman
Updated: 02/08/2018
Description: Main file for Twitter Art Bot
'''
import praw
import tweepy
from instance import *

GO = True



while(GO):

    
    reddit = RedditInstance().reddit_instance
 

    twitter = TwitterInstance().twitter_instance
    
    new_post = ""

    print(reddit.read_only)
    for submission in reddit.subreddit('art').top(time_filter='week',limit=1):
        new_post = submission.title + " " +submission.url

    twitter.update_status(new_post)


      
    GO = False

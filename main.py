'''
Author: Josh Eastman
Updated: 02/08/2018
Description: Main file for Twitter Art Bot
'''
import os
import praw
import tweepy
import urllib
from instance import *

GO = True

reddit = RedditInstance().reddit_instance
twitter = TwitterInstance().twitter_instance


while(GO):    
    new_post = ''
    url = ''

    print(reddit.read_only)
    for submission in reddit.subreddit('pics').top(time_filter='week',limit=5):
        url = submission.url
        
        new_post = submission.title + '' +submission.url

    image = url.replace('https://i.redd.it/','')

    urllib.request.urlretrieve(url,image)
    os.rename(image, "images/"+image)

      
    GO = False


#    urllib.request.urlretrieve(url,"39XeDFj.jpg")
#
#    twitter.update_with_media("39XeDFj.jpg","test")

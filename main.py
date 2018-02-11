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
from link_image_handling import *

GO = True

reddit = RedditInstance().reddit_instance
twitter = TwitterInstance().twitter_instance

last_url = ''


while(GO):    
    new_post = ''
    url = ''
##
##    print(reddit.read_only)
##    for submission in reddit.subreddit('pics').hot(limit=5):
##        url = submission.url
##        
##        new_post = submission.title + ' ' + submission.url
##
##        print(new_post)

    url = 'https://imgur.com/OyKKLKg'
    result = handleLink(url)
    print(result[0])
    print(result[1])
    print(result[2])



    
##    fixed_url = url[:8] + 'i.' + url[8:] + '.jpg'
##    image = fixed_url[20:]
##    print(image)

   # urllib.request.urlretrieve(url,image)
 #   os.rename('OyKKLKg.jpg', 'images/OyKKLKg.jpg')
      
    GO = False


#    urllib.request.urlretrieve(url,"39XeDFj.jpg")
#
#    twitter.update_with_media("39XeDFj.jpg","test")



    
        
    

    

    
#imgur 'https://i.imgur.com/OyKKLKg.jpg','OyKKLKg.jpg'
#for imgur, add i. & .jpg to url, strip everything but id & .jpg from from url for image


#For reddit, strip all but identifier, done.

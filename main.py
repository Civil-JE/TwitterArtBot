'''
Author: Josh Eastman
Updated: 02/12/2018
Description: Main file for Twitter Art Bot
'''
import os
import praw
import tweepy
from instance import *
from link_image_handling import *

GO = True
IMAGE_DIRECTORY = 'images\\' #Change 'images/' to your preferred image storage location

reddit = RedditInstance().reddit_instance
twitter = TwitterInstance().twitter_instance

#Keep last URL so it doesn't post twice.
#To-Do: Find a way to compare images
last_url = ''

while(GO):    
    new_post = ''
    is_new_post = False
    new_submission = None
    i = 1
    subreddit = 'pics'

    while not(is_new_post):
        #Grab a post or multiple posts. If it's the same as the last post, try again.
        for submission in reddit.subreddit(subreddit).hot(limit=i):
            #Get the URL that hopefully leads to an image
            new_submission = submission  
            
        if(last_url == submission.url ):
            is_new_post = False
            i = i + 1
            print('Duplciate Post.' + 'Take #' + str(i))
        else:
            print('New Post!')
            is_new_post = True

    #Take the URL and return a usable image location and link.
    link_result = handleLink(new_submission.url)

    #Make sure the handleLink didn't fail, the move onto getting the image
    if(link_result[0]):
        image_result = getImage(link_result[1], link_result[2], IMAGE_DIRECTORY)

        #Make sure getting the image didn't fail, then move onto preparing the tweet
        if(image_result[0]):
            new_tweet = prepareTweet(new_submission.title, link_result[1], subreddit)

            #Make sure preparing the tweet didn't fail, then move onto sending the tweet
            if(new_tweet[0]):
                print('#########################################################')
                print('Tweeting \n'+ new_tweet[1] + '\n' + image_result[1])
                print('#########################################################')
                tweet_result = twitter.update_with_media(image_result[1],new_tweet[1])
                
            else:
                print('ERROR: ' + new_tweet[1] + ' | ' + new_tweet[2])          
        else:
            print('ERROR: ' + image_result[1] + ' | ' + image_result[2])        
    else:
        print('ERROR: ' + link_result[1] + ' | ' + link_result[2])

    GO = False
    
    


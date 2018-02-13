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
IMAGE_DIRECTORY = 'images\\' #Change 'images\' to your preferred image storage location

reddit = RedditInstance().reddit_instance
twitter = TwitterInstance().twitter_instance

#Keep last URL so it doesn't post twice.
#To-Do: Find a way to compare images
last_post = ''
i = 1

while(GO):    
    new_post = ''
    is_posted = False
    new_submission = None  
    subreddit = 'art'

    while not(is_posted):
        #Grab a post or multiple posts. If it's the same as the last post, try again.
        for idx, submission in enumerate(reddit.subreddit(subreddit).hot(limit=i)):
            if(idx != i-1):
                continue
            
            #Get the URL that hopefully leads to an image
            new_submission = submission  
            
            if(last_post == submission.url ):
                print('Duplciate Post.' + 'Take #' + str(i))
                i = i + 1
                continue
            else:
                print('New Post!')

                #Take the URL and return a usable image location and link.
                link_result = handleLink(new_submission.url)

                #Make sure the handleLink didn't fail, the move onto getting the image
                if(link_result[0]):
                    image_result = getImage(link_result[1], link_result[2], IMAGE_DIRECTORY)
                else:
                    print('ERROR: ' + link_result[1] + ' | ' + link_result[2])
                    i = i + 1
                    last_post = new_submission.url
                    continue
                
                    #Make sure getting the image didn't fail, then move onto preparing the tweet
                if(image_result[0]):
                    new_tweet = prepareTweet(new_submission.title, link_result[1], subreddit)
                else:
                    print('ERROR: ' + image_result[1] + ' | ' + image_result[2])
                    i = i + 1
                    last_post = new_submission.url
                    continue
                
                #Make sure preparing the tweet didn't fail, then move onto sending the tweet
                if(new_tweet[0]):
                    print('#########################################################')
                    print('Tweeting \n'+ new_tweet[1] + '\n' + image_result[1])
                    print('#########################################################')
                    #tweet_result = twitter.update_with_media(image_result[1],new_tweet[1])
                    is_posted = True
                    i=1
                    GO = False
                    break
                    
                else:
                    print('ERROR: ' + new_tweet[1] + ' | ' + new_tweet[2])
                    last_post = new_submission.url
                    continue
                   

    
    


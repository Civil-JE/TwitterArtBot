###
# Author: Josh Eastman
# Updated: 02/16/18
# Version 1.0.0
# Description: Based on link_image_handling from TwitterArtBot. Used to deal with the link provided
# by PRAW and download the images.
###
import urllib.request
import os
import logging
import shutil


# If a link does not have .jpg at the end, add it
def check_if_extension(url):
    url_length = len(url)
    if url[url_length - 4] != '.' and url[url_length - 5] != '.':
        return False
    else:
        return True


def handle_link(url):
    # Check if imgur or reddit
    # To-Do: Add more sites for better compatibility
    try:
        # Checks for the various states the imgur url can come in
        if url.find('imgur') != -1:
            if not check_if_extension(url):
                url = url + '.jpg'
            if url[-4:] == 'gifv':
                url = url[:-4] + 'mp4'
            if url[9] != '.':
                url = url[:8] + 'i.' + url[8:]
            image = url[20:]

            return [True, url, image]  # boolean for whether or not it failed

        elif url.find('redd.it') != -1:
            if url[8] == 'v':
                return[False, url, 'Not supported']
            else:
                image = url[18:]  # for imgur image, strip everything but id and .jpg
                return [True, url, image]  # boolean for whether or not it failed

        elif url.find('gfycat'):
            url = url + '.webm'
            if url[:13].find('giant') == -1:
                url = url[:8] + 'giant.' + url[8:]
            image = url[25:]
            return [True, url, image]  # boolean for whether or not it failed

        else:
            # If not from a supported url, return False
            return [False, url, 'Not supported:']

    except:
        return [False, 'Unidentified error during handleLink', url]


# Moves the downloaded image to wherever you would like to store it.
# No longer needed
def move_image(image_name, image_directory):
    file_location = image_directory + image_name

    try:
        os.rename(image_name, file_location)

        return [True, file_location, 'Moved image to ' + file_location]
    except:
        os.remove(image_name)
        logging.warning(image_name + ' was deleted.')
        return [False, file_location, 'Failed to move file']


# Finds the image from the url and downloads it.
def get_image(url, image_location, image_directory):
    try:
        urllib.request.urlretrieve(url, image_directory + image_location)
        logging.info(image_location + ' was downloaded.')
        return [True, image_directory + image_location, 'Obtained and moved image to image folder']

    except:
        return [False, url, 'Failed to get image']


# Sort all of the downloaded images into two categories
def sort_downloads(image_directory):
    for filename in os.listdir(image_directory):
        if filename[-4:].find('jpg') == 1 or filename[-4:].find('png') == 1 or filename[-4:].find('gif') == 1:
            shutil.move(image_directory + filename, image_directory + 'pictures/')
        elif filename[-5:].find('webm') == 1 or filename[-4:].find('mp4') == 1:
            shutil.move(image_directory + filename, image_directory + 'vids/')


# Formats the tweet to prepare to send.  Include source if possible.
def prepare_tweet(submission):
    try:
        tweet_text = (submission.title + '\nThis was posted by ' + submission.author.name + ' on '
                      + '/r/' + submission.subreddit.display_name + '.\n' + submission.url)
        return [True, tweet_text, 'Tweet created successfully']
    except:
        return [False, tweet_text, 'Error creating tweet (link_image_handling > prepareTweet)']


# download image for each submission
def download_all(submission, image_directory):
    link_result = handle_link(submission.url)
    # Make sure the handleLink didn't fail, the move onto getting the image
    if link_result[0]:
        get_image(link_result[1], link_result[2], image_directory)
        logging.info('{0} | {1}'.format(link_result[1], link_result[2]))
    else:
        logging.error('{0} | {1}'.format(link_result[1], link_result[2]))

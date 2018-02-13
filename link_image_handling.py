import urllib.request
import os

#If a link does not have .jpg at the end, add it
def ifNoExtensionAdd(url):
    if url[-4:] != '.jpg' and url[-4:] != '.png':
        new_url = url + '.jpg' 
        return new_url
    else:
        return url

def handleLink(url):
    #Check if imgur or reddit
    #To-Do: Add more sites for better compatiblity
    try:
        #Checks for the various states the imgur url can come in
        if url.find('i.imgur') != -1:
            fixed_url = ifNoExtensionAdd(url)
            image = fixed_url[20:]  #for imgur image, strip everything but id and .jpg
            return [True, fixed_url, image] #boolean for whether or not it failed
        
        elif url.find('imgur') != -1:
            jpg_url = ifNoExtensionAdd(url)       
            fixed_url = jpg_url[:8] + 'i.' + jpg_url[8:]  #Add i to imgur link if it's not there.          
            image = fixed_url[20:]  #for imgur image, strip everything but id and .jpg
            return [True, fixed_url, image] #boolean for whether or not it failed

        elif url.find('redd.it') != -1:
            fixed_url = ifNoExtensionAdd(url)            
            image = fixed_url[18:]  #for imgur image, strip everything but id and .jpg
            return [True, fixed_url, image] #boolean for whether or not it failed   
        else:
            #If not from a supported url, return False
            return [False, url, 'Not supported:']
        
    except:
        return[False, 'Unidentified error during handleLink', url]

#Moves the downloaded image to whever you would like to store it.
def moveImage(image_name, image_directory):
    file_location =  image_directory + image_name
    
    try:
        os.rename(image_name, file_location)
        
        return [True, file_location, 'Moved image to ' + file_location]
    except:
        return [False, file_location, 'Failed to move file']

#Finds the image from the url and downloads it.
def getImage(url, image_location, image_directory):
    try:
        urllib.request.urlretrieve(url, image_location)
        image_moved = moveImage(image_location, image_directory)

        if(image_moved[0]):
            return [True, image_moved[1], 'Obtained and moved image to image folder']           
        else:
            return [False, url, image_moved[2] + ' | ' + image_moved[1]]
    except:
        return [False, url, 'Failed to get image']
    
#Formats the tweet to prepare to send.
def prepareTweet(title, url, source):
    #Include source if possible.
    try:
        tweet_text = title + '\nThis was posted at ' + url + '.\n' + 'Found on Reddit.com/r/' + source
        return [True, tweet_text]
    except:
        return [False, 'Error creating tweet (link_image_handling > prepareTweet)']
    
    
    

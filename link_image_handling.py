def handleLink(url):
    #Check if imgur or reddit
    try:
        if url.find('imgur'):
            #if imgur, check if i.imgur and if not add i. to front of url after https and .jpg to end.       
            fixed_url = url[:8] + 'i.' + url[8:] + '.jpg'
            
            #for imgur image, strip everything but id and .jpg
            image = fixed_url[20:]
            
            return [True, fixed_url, image] #boolean for whether or not it failed
        elif url.find('reddit'):
            #if reddit, check if i.reddit do nothing to url. for image strip everything but id+.jpg
            image = url[18:] + '.jpg'
            
            return [True, url, image]
        
            #i.reddit url.replace('https://i.redd.it/','')
        else:
            #If not from a supported url, return False
            return [False, 'Not supported:', url]
        
    except:
        print('Unidentified error during handleLink')
        print(url)
        return[False, 'Unidentified error during handleLink', url]

def moveImage(image_name):
    try:
        file_location = 'images/' + image_name #Change 'images/' to your preferred image storage
        os.rename(image_name, 'images/'+image_name)
        
        return [True, Moved image to ' + file location]
    except:
        return [False, 'Failed to move file']
    
    

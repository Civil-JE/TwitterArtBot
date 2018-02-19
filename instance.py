import praw
import tweepy


class RedditInstance:
    # Information is read from Credentials.txt
    client_id = ""
    client_secret = ""
    user_agent = ""
    username = ""
    password = ""

    reddit_instance = None

    def __init__(self):
        credentials_file = "credentials/Credentials.txt"  # Prod
        # credentials_file = "credentials/testCredentials.txt" # Test
        opened_file = open(credentials_file, "r")
        credentials = opened_file.readlines()

        # Had to add .strip to remove invisible whitespaces/leading characters
        self.client_id = credentials[0].strip()
        self.client_secret = credentials[1].strip()
        self.user_agent = credentials[2].strip()
        # self.username = credentials[3].strip()
        # self.password = credentials[4].strip()

        # Don't need to provide user details due to only needing a Read Only instance.
        self.reddit_instance = praw.Reddit(client_id=self.client_id, client_secret=self.client_secret,
                                           user_agent=self.user_agent)


class TwitterInstance:
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""

    twitter_instance = None

    def __init__(self):
        # credentials_file = "credentials/Credentials.txt" #Prod
        credentials_file = "credentials/testCredentials.txt"  # Test
        opened_file = open(credentials_file, "r")
        credentials = opened_file.readlines()

        self.consumer_key = credentials[6].strip()
        self.consumer_secret = credentials[7].strip()
        self.access_token = credentials[8].strip()
        self.access_token_secret = credentials[9].strip()

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        self.twitter_instance = tweepy.API(auth)

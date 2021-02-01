from splitvideo import VideoSplit

import tweepy

CONSUMER_KEY = 'YOUR_KEY'
CONSUMER_SECRET = 'YOUR_KEY'
ACCESS_TOKEN = 'YOUR_KEY-h7sLGGoIV9WxJzWPCq6JmFkJN5KXJ3'
ACCESS_TOKEN_SECRET = 'YOUR_KEY'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

video = VideoSplit()
path = video.getPathOfEpisode()
nametweet = video.getNameofTweet()

# Create a tweet
api.update_with_media(path, nametweet)







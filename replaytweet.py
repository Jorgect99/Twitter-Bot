from splitvideo import VideoSplit
import time
import tweepy

CONSUMER_KEY = 'LgZE0F6l294LR83rDwRzLn9kA'
CONSUMER_SECRET = 'xjRe2h7tIIAuWdTnP0jwwq46qD5Bynt4BsQ1z7KbAc5DE2wlF1'
ACCESS_TOKEN = '1322450724484116482-h7sLGGoIV9WxJzWPCq6JmFkJN5KXJ3'
ACCESS_TOKEN_SECRET = 'Q6ICjRKiEb2OeBmOYDY0vu4uh3CUQzVCHsL7SmBO9Psx8'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

video = VideoSplit()
path = video.getPathOfEpisode()
nametweet = video.getNameofTweet()

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#hellobillybot' in mention.full_text.lower():
            print('found #hellobillybot')
            textreplay = '@' + mention.user.screen_name + ' Hello back to you!' 
            api.update_with_media(path, textreplay, in_reply_to_status_id=mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)



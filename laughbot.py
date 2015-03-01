import tweepy, time, sys

CONSUMER_KEY = "..."
CONSUMER_SECRET = "..."
ACCESS_KEY = "..."
ACCESS_SECRET = "..."

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

#testTweet = "Wugbot says hello!"
#api.update_status(testTweet)

#NLTK Chapter 3, Exercise 27
import random
def laughter(n):
    laugh= ""
    while len(laugh) < n:
        laugh = laugh + random.choice('aehh ')
    return laugh

x = -1
while x < 0:
    laughLength = random.randint(2,140)
    api.update_status(laughter(laughLength))


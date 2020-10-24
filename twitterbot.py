import tweepy
import time
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(key,secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

search = ['#AWSUserGroup','#awsmmetups','#awscommunity', "#awsug"]
nrTweets = 10

for i in range(0,len(search)):
    for tweet in tweepy.Cursor(api.search, search[i]).items(nrTweets):
        try:
            print('Tweet Liked')
            tweet.favorite()
            tweet.retweet()
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

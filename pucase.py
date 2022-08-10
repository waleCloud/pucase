import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

def authenticate():
  # keys and tokens from the Twitter Dev Console
  consumer_key = '4KzIFprHyNApHjsXOg1OEfJ3c'
  consumer_secret = 'hpBzI2SicsaNqIluwWeK3nySKiDHvSBXmSamKT1cppcXceh59J'
  access_token = '197883124-T8c2XZT0Aa3WGl5cm4Xoe2LZp36lvn5wayU6dHq9'
  access_token_secret = 'NQiqWjqqPkjPgvC7xgZBHHhWaVMqmMSDM6CDf2YDFnAGC'

  # attempt authentication
  try:
    # create OAuthHandler object
    auth = OAuthHandler(consumer_key, consumer_secret)
    # set access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # create tweepy API object to fetch tweets
    print("Authenticating...")
    authVal = tweepy.API(auth)
    print("Auth value:....   ", authVal)

  except:
    print("Error: Authentication Failed")

def clean_tweet(tweet):
  '''
  Utility function to clean tweet text by removing links, special characters
  using simple regex statements.
  '''
  return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
  '''
  Utility function to classify sentiment of passed tweet
  using textblob's sentiment method
  '''
  # create TextBlob object of passed tweet text
  analysis = TextBlob(clean_tweet(tweet))
  # set sentiment
  if analysis.sentiment.polarity > 0:
    return 'positive'
  elif analysis.sentiment.polarity == 0:
    return 'neutral'
  else:
    return 'negative'

def get_tweets(query, count = 10):
  '''
  Main function to fetch tweets and parse them.
  '''
  # empty list to store parsed tweets
  tweets = []

  try:
    # call twitter api to fetch tweets
    fetched_tweets = search(q = query, count = count)

    # parsing tweets one by one
    for tweet in fetched_tweets:
      # empty dictionary to store required params of a tweet
      parsed_tweet = {}

      # saving text of tweet
      parsed_tweet['text'] = tweet.text
      # saving sentiment of tweet
      parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

      # appending parsed tweet to tweets list
      if tweet.retweet_count > 0:
        # if tweet has retweets, ensure that it is appended only once
        if parsed_tweet not in tweets:
          tweets.append(parsed_tweet)
      else:
        tweets.append(parsed_tweet)

    # return parsed tweets
    return tweets

  except:
    # print error (if any)
    print("Error getting tweets")

# def sentiment_analysis():

#   # calling function to get tweets
#   tweets = get_tweets(query = 'Education', count = 200)

#   # picking positive tweets from tweets
#   ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
#   # percentage of positive tweets
#   print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
#   # picking negative tweets from tweets
#   ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
#   # percentage of negative tweets
#   print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
#   # percentage of neutral tweets
#   print("Neutral tweets percentage: {} % \
#     ".format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets)))

#   # printing first 5 positive tweets
#   print("\n\nPositive tweets:")
#   for tweet in ptweets[:10]:
#     print(tweet['text'])

#   # printing first 5 negative tweets
#   print("\n\nNegative tweets:")
#   for tweet in ntweets[:10]:
#     print(tweet['text'])


def main():
  authenticate();

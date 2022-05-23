import tweepy

consumer_key = 'change with your consumer key'
consumer_secret = 'change with your consumer secret'
access_token = 'change with your access token'
access_secret = 'change with your access secret'
tweetsPerQry = 100
maxTweets = 10000
hashtag = "#covid19"

authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)
maxId = -1
tweetCount = 0
while tweetCount < maxTweets:
    if(maxId <= 0):
        newTweets = api.search_tweets(q=hashtag, count=tweetsPerQry,
                                      result_type="mixed", tweet_mode="extended", lang="pt-br")
    else:
        newTweets = api.search_tweets(q=hashtag, count=tweetsPerQry, max_id=str(
            maxId - 1), result_type="mixed", tweet_mode="extended", lang="pt-br")

    if not newTweets:
        print("Tweet Habis")
        break

    for tweet in newTweets:
        print(tweet.full_text.encode('ascii', 'ignore'))

    tweetCount += len(newTweets)
    maxId = newTweets[-1].id

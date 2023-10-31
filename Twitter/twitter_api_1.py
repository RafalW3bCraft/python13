import tweepy

#bearer_token = "AAAAAAAAAAAAAAAAAAAAAHP1qgEAAAAAthcuRpt%2Bdw1m1b%2FadBU%2BrOUGxSc%3D1KYBsnoxHNdME5m1DtgjLPLjv0EdQnlu7SYoivJ4mZAVkFj5Me"

consumer_key = "T0O0kBC6L6Y9364XvB4ZCmjOE"
consumer_secret = "3k0NpzAZucwclKgFNEkDv010UCxj2gNy0N7FngrZbpe2xmuGPu"

access_token = "1647893887401472000-Izrux3KdZ2yLTErxM1v2uIpX0eCrJP"
access_token_secret = "6DKqlA7lWdyGIY9CLvOQGnQIWorsafBZUA6cRyWj3uyP3"
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

user = 'veritasium'
limit =100

tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')
columns = ['User', 'Tweet']
data = []
for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])
df = pd.DataFrame(data, columns=columns)

print(df)
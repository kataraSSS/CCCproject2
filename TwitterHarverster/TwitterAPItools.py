from CouchDBtools import *
import tweepy
from time import sleep
from tweepy.streaming import StreamListener
from tweepy import Stream


# Variables that contains the user credentials to access Twitter API
consumer_key = 'xjOiODN7QXUWNW1TS7Yy7BFgj'
consumer_secret = 'VvvEYbUCBSNIBTynZZWVmqxjvYx04CasXV1I0PG8PkbGakiLJt'
access_token_key = '1119208072763756545-j8CZp18HWbujs5blyzm9ww3fzudbl3'
access_token_secret = 'Fx4xEfVE5WO8xhBU0cFeT8UsJvHV5vMTUVkkuhPa2CwIO'

auth = tweepy.OAuthHandler( consumer_key, consumer_secret )
auth.set_access_token( access_token_key, access_token_secret )
api = tweepy.API( auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True )

# connect to Twitter API
# Create authentication objects
# 创建认证对象
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# 设置你的access token和access secret
auth.set_access_token(access_token_key, access_token_secret)
# 传入auth参数，创建API对象
api = tweepy.API(auth)


def showMytweets():
    public_tweets = api.home_timeline()
    # 遍历所拉取的全部微博
    for tweet in public_tweets:
       # 打印存在微博对象中的text字段
       print(tweet.text)


def Tsearch(query = 'china',language = "en"):
    # 你想查找的关键字  query = "sports"
    # 语言代码（遵循ISO 639-1标准）   language = "en"
    # 使用上面的参数，调用user_timeline函数
    results = api.search(q=query, lang=language)


    # 遍历所拉取的全部twitter
    for tweet in results:
       # 打印存在微博对象中的text字段
       print(tweet.user.screen_name,"Tweeted:",tweet.text)
    return results

def Tgeo(geo):

    api.reverse_geocode(granularity='city',)

class listener(StreamListener):

    def on_data(self, data):
        #print(type(data)) # --> str
        pushToCouchDB(data)


    def on_error(self, status):
        print(status)

    def on_timeout(self):
        print("~~~~~~~~Timeout, sleeping for 100 seconds...\n")
        sleep(100)
        return

def beginStream():
    twitterStream = Stream(auth, listener())
    #track=["sports"]
    mel = [144.59,-38.43,145.51,-37.51]
    syd = [150.52,-34.12,151.34,-33.58]
    vic = [140.96,-39.18,144.04,-33.98,144.04,-39.16,149.98,-35.91]
    aus = [105.033007,-42.384930,153.844606,-10.466363]
    twitterStream.filter(locations= aus)













# How to access Twitter data using the module tweepy
# Twitter no longer allows unauthenticated access, you need something called OAuth
# You need to create a (bogus) application on https://dev.twitter.com/apps to get the OAuth keys

consumerKey = 'i8XVJgx2YtZGpZq6Ce79dg' 
consumerSecret = 'RWuG21WuPGj4L5RJJqvi2TQnf3pWYq41dDbJL2tk'
accessToken = '26716739-voxrImM5E58OpoCBu74TCelxgvMszvPoJefYkVwJO'
accessTokenSecret = 'fyGrkwWZXCN25K3hkFgEbwxPvMX0UGx5LTR7uAJyiU'    

import tweepy
 
auth1 = tweepy.auth.OAuthHandler(consumerKey,consumerSecret)
auth1.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth1)
#api.update_status('This is a test!') # Will send a Tweet

myFollower = api.followers()[0]
myFollowerInfo = myFollower.__getstate__()

# Read tweets
listener = tweepy.StreamListener()



# SixOhSix twitter module as used by the book Mining the Social Web
import twitter
twitter_api = twitter.Twitter(domain="api.twitter.com", api_version='1')
trends = twitter_api.trends()


import twitter
twitter_api=twitter.Twitter(domain="api.twitter.com", api_version='1')
WORLD_WOE_ID = 1 # The Yahoo! Where On Earth ID for the entire world
world_trends = twitter_api.trends._(WORLD_WOE_ID) # get back a callable
[ trend for trend in world_trends()[0]['trends'] ] 

twitter_search = twitter.Twitter(domain = "search.twitter.com")
search_results = []
for page in range(1,6):
    search_results.append(twitter_search.search(q="SNL", rpp= 100,page=page))
    
len(search_results) # Number of pages of search results
# same output as going through https://search.twitter.com/search.json?q=SNL&rpp=100&page=1 etc

import json # Builtin module for JSONs
print json.dumps(search_results, sort_keys=True, indent=1)   
tweets = [r['text'] for result in search_results for r in result['results']]

tweets[-1] # unicode for the last tweet
print tweets[-1] # Readable text
tweets[-1][100:110] # Picks out characters, tweets[-1] is a string

# strings and Unicode
s1 = "his son's friend"
type(s1)
print s1
s1unicode = u'his son\u2019s friend'
type(s1unicode)
print s1unicode

s2 = "hej där"
type(s2)
print s2
s2.encode('utf-8')
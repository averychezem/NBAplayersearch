#Avery Chezem and George Dant -- Final Project CS229

## Get input from user
inputname = input("What NBA team would you like to gather information on? ")
## check if input is valid

def validinput(giventeam):
   list_of_teams = ['Hawks', 'Atlanta Hawks', 'Celtics', 'Boston Celtics', 'Nets', 'Brooklyn Nets', 'Hornets', 'Charlotte Hornets', 'Bulls', 'Chicago Bulls', 'Cleveland Cavaliers', 'Cavs', 'Cavaliers', 'Dallas Mavericks', 'Mavs', 'Mavericks', 'Denver Nuggets', 'Nuggets', 'Pistons', 'Detroit Pistons', 'Golden State', 'Golden State Warriors', 'Warriors', 'Houston Rockets', 'Rockets', 'Indiana Pacers', 'Pacers', 'LA Clippers', 'Clippers', 'Los Angeles Lakers', 'Lakers', 'Memphis', 'Memphis Grizzlies', 'Miami Heat', 'Heat', 'Milwaukee Bucks', 'Bucks', 'Minnesota Timberwolves', 'Timberwolves', 'New Orleans Pelicans', 'Pelicans', 'New York Knicks', 'Knicks', 'Oklahoma City Thunder', 'Thunder', 'OKC', 'Orlando Magic', 'Magic', 'Philadelphia 76ers', '76ers', 'Phoenix Suns', 'Suns', 'Portland Trail Blazers', 'Trail Blazers', 'Sacromento Kings', 'Kings', 'San Antonio Spurs', 'Spurs', 'Toronto Raptors', 'Raptors', 'Utah Jazz', 'Jazz', 'Washington Wizards', 'Wizards']
   if giventeam not in list_of_teams:
      exit( "That is not a valid NBA team")

runs = validinput(inputname)
##___________________________________________________________________________
#WIKIPEDIA
## Programming Languages in Wikipedia
import requests, json, re
import os.path
from pprint import pprint
from bs4 import BeautifulSoup

# The following function takes as input a full URL.
# It returns a BeautifulSoup object representing that web page's contents
# If the page does not exist, it returns None
def getPage(url):
   req = requests.get(url)
   if (req.status_code != 200):
      return None
   return BeautifulSoup(req.content, 'html.parser')

## You will need to add this to the relative links you may encounter
baseUrl = "https://en.wikipedia.org"

## This page contains a list of all NBA Rosters that have Wikipedia pages
listPage = getPage(baseUrl + "/wiki/List_of_current_NBA_team_rosters")


## Get Team Sections
teams = listPage.find_all("h4")
# print(len(teams)) ## should be 30
# print(teams[0].get_text()) ## should give Celtics info
# print(teams[0])

def getTeamId(teams, name):
   for team in range(len(teams)):
      if name in teams[team].get_text():
         return team
   return -1

#
def makeObjectfromitem(item):
   tds = item.find_all('td')
   return {'Position': tds[0].get_text(), 'Number' : tds[1].get_text(), 'Name':tds[2].get_text()}


# players (
def getPlayerFromTeam(team):
   return [
      makeObjectfromitem(item)
      for item in team.find_all("tr")
      if item.th is None
   ]

anyTeam = getPlayerFromTeam(teams[getTeamId(teams, inputname)].next_sibling.next_sibling)
print(anyTeam)

#____________________________________________________________________________
# #TWITTER
# #!/usr/bin/python3
# # Accessing the Twitter API
# # This script describes the basic methodology for accessing a Twitter feed
# # or something similar.

# # Loading libraries needed for authentication and requests
# from requests_oauthlib import OAuth2Session
# from oauthlib.oauth2 import BackendApplicationClient
# import json

# # In order to use this script, you must:
# # - Have a Twitter account and create an app
# # - Store in keys.json a property called "twitter" whose value is an
# #     object with two keys, "key" and "secret"
# with open('keys.json', 'r') as f:
#    keys = json.loads(f.read())['twitter']

# twitter_key = keys['key']
# twitter_secret = keys['secret']

# # We authenticate ourselves with the above credentials
# # We will demystify this process later
# #
# # For documentation, see http://requests-oauthlib.readthedocs.io/en/latest/api.html
# # and http://docs.python-requests.org/en/master/
# client = BackendApplicationClient(client_id=twitter_key)
# oauth = OAuth2Session(client=client)
# token = oauth.fetch_token(token_url='https://api.twitter.com/oauth2/token',
#                           client_id=twitter_key,
#                           client_secret=twitter_secret)

# # Base url needed for all subsequent queries
# base_url = 'https://api.twitter.com/1.1/'

# # Particular page requested. The specific query string will be
# # appended to that.
# page = 'search/tweets.json'

# #Makes query with input from user
# query = '?q=%s&tweet_mode=extended&count=100'%inputname

# # Depending on the query we are interested in, we append the necessary string
# # As you read through the twitter API, you'll find more possibilities
# req_url = base_url + page + query

# # We perform a request. Contains standard HTTP information
# response = oauth.get(req_url)

# # Read the query results
# results = json.loads(response.content.decode('utf-8'))

# ## Process the results
# ## CAUTION: The following code will attempt to read up to 10000 tweets that
# ## Mention Hanover College. You should NOT change this code.
# tweets = results['statuses']
# while True:
#    if not ('next_results' in results['search_metadata']):
#       break
#    if len(tweets) > 10000:
#       break
#    next_search = base_url + page + results['search_metadata']['next_results'] + '&tweet_mode=extended'
#    print(results['search_metadata']['next_results'])
#    response = oauth.get(next_search)
#    results = json.loads(response.content.decode('utf-8'))
#    tweets.extend(results['statuses'])

# ## CAUTION: For the rest of this assignment, the list "tweets" contains all the
# ## tweets you would want to work with. Do NOT change the list or the value of "tweets".

# ## list comprehension that will produce a list containing all the texts from the tweets
# texts = [tweet['full_text'] for tweet in tweets]

# ## returns the full texts of the tweets
# def get_full_text(tweet):
#   if 'retweeted_status' in tweet.keys():
#     full_text = tweet['retweeted_status']['full_text']
#     return(full_text)
#   else:
#     full_text = tweet['full_text']
#     return(full_text)

# full_texts_list = [get_full_text(tweet) for tweet in tweets]

# def tags_per_tweet_function(tweet):
#   hashtag_list = []
#   hashtags = tweet['entities']['hashtags']
#   for i in range(len(hashtags)):
#       hashtag_list.append(tweet['entities']['hashtags'][i]['text'])
#   return hashtag_list

# tags_per_tweet = [tags_per_tweet_function(tweet) for tweet in tweets]

# def tweet_information_function(tweet):
#   tweet_dict = {}
#   tweet_dict['text'] = get_full_text(tweet)
#   tweet_dict['author'] = tweet['user']['screen_name']
#   tweet_dict['date'] = tweet['created_at']
#   tweet_dict['hashtags'] = tags_per_tweet_function(tweet)
#   tweet_dict['mentions'] = [user['screen_name'] for user in tweet['entities']['user_mentions']]
#   return tweet_dict

# tweet_information = [tweet_information_function(tweet) for tweet in tweets]

# with open('NBA_Team_Tweets.json', 'w') as file:
#   json.dump(tweet_information, file)
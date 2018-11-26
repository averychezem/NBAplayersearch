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

## This page contains a list of all programming languages that have Wikipedia pages
listPage = getPage(baseUrl + "/wiki/List_of_current_NBA_team_rosters")
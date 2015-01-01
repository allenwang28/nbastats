from bs4 import BeautifulSoup
from urllib2 import urlopen
import time
from datetime import date
from team import Team
import re

BASE_URL="http://www.basketball-reference.com/"

def year():
    today = date.today()
    year = today.year
    if today.month >= 9:
        year += 1
    return year


def Soup():
    html = urlopen(BASE_URL + 'leagues/NBA_' + str(year()) + '.html').read()
    soup = BeautifulSoup(html, "lxml")
    return soup 

# def team_names():
#    soup = Soup() 
#    return [team.string for team in soup.find('div', id="all_standings").find_all('a')]

# NOTICE: stats are returned in an array of strings, not integers
def stats(team_name):
    soup = Soup() 
    return [team.string for team in soup.find(text = re.compile(team_name)).find_all_next("td", limit = 7)]

def team_stats(team_name):
    soup = Soup()
    return [team.string for team in soup.find('div', id="all_team_stats").find(text = re.compile(team_name)).find_all_next("td", limit = 24)]

if __name__ == "__main__":
    

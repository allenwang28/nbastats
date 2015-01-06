from bs4 import BeautifulSoup
from urllib2 import urlopen
import time
from datetime import date
from team import Team
import re

BASE_URL="http://www.basketball-reference.com/leagues/NBA_"

def year():
    today = date.today()
    year = today.year
    if today.month >= 9:
        year += 1
    return year


def base_soup():
    html = urlopen(BASE_URL + str(year()) + '.html').read()
    soup = BeautifulSoup(html, "lxml")
    return soup 

def records_soup():
    html = urlopen(BASE_URL + str(year()) + '_games.html').read()
    soup = BeautifulSoup(html, "lxml")
    return soup

def all_wins_losses():
    soup = base_soup()
    team_stats = {}
    for team in Team.team_names:
        team_stats[team] = {}
        team_stats[team]['W'] = int(soup.find(text = re.compile(team)).find_next("td").string)
        team_stats[team]['L'] = int(soup.find(text = re.compile(team)).find_next("td").find_next("td").string)
        team_stats[team]['%'] = float(team_stats[team]['W'])/(float(team_stats[team]['L']) + float(team_stats[team]['W']))
    return team_stats 

def process_calendar():
    soup = records_soup()
    elem_list = [elem.string for elem in soup.find("tbody").find_all_next("td")]
    games = []
    i = 0
    while i < len(elem_list): 
        entry = {}
        entry['Date'] = elem_list[i]

        if(elem_list[i + 3]):
            entry['P?'] = True
            score1 = (elem_list[i + 3])
            score2 = (elem_list[i + 5])
            if int(score1) > int(score2):
                entry['W'] = elem_list[i + 2]
                entry['L'] = elem_list[i + 4]
            else:
                entry['L'] = elem_list[i + 2]
                entry['W'] = elem_list[i + 4]
        else:
            entry['P?'] = False
            entry['W'] = elem_list[i + 2]
            entry['L'] = elem_list[i + 4]

        games.append(entry)
        i += 8
    return games


if __name__ == "__main__":
    print all_wins_losses()

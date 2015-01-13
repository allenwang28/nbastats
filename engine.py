import scraper
from team import Team
import re
def initialize_teams():
    teams = {}
    i = 0
    team_records = scraper.all_wins_losses()

    for team_name in Team.team_names:
        # print "Processing: " + team_name
        teams[team_name] = (Team(team_name, Team.divisions[i/5], team_records[team_name]))
        i += 1
    order_teams(teams)
    return teams 

def east_teams(t):
    east = []
    teams = []
    for team in Team.team_names:
        teams.append(t[team])

    for team in teams:
        if team.conference() == "East":
            east.append(team)
    merge_sort(east) 
    return east

def west_teams(t):
    west = []
    teams = []
    for team in Team.team_names:
        teams.append(t[team])

    for team in teams:
        if team.conference() == "West":
            west.append(team)
    merge_sort(west)
    return west

def merge_sort(teams):
    if len(teams) <= 1:
        return
    mid = len(teams)/2
    left = teams[:mid]
    right = teams[mid:]
    merge_sort(left)
    merge_sort(right)
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            teams[k] = left[i]
            i += 1
        else:
            teams[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        teams[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        teams[k] = right[j]
        j += 1
        k += 1

def order_teams(team_hash = {}):
    teams = []
    for team in Team.team_names:
        teams.append(team_hash[team])
    east_teams = []
    west_teams = []
    for team in teams:
        if team.conference() == "West": # O(N) time to find the conference
            west_teams.append(team)
        else:
            east_teams.append(team)
    merge_sort(west_teams)
    merge_sort(east_teams)
    i = 1
    for team in west_teams:
        team.set_seed(i)
        i += 1
    i = 1
    for team in east_teams:
        team.set_seed(i)
        i += 1
    return { "East": east_teams, "West": west_teams }
    
def summarize_teams(teams):
    for team in teams:
        summarize_team(team)

def summarize_team(team):
    print team.name + ": "
    print "Division: " + team.division + " (" + str(team.seed) + " seed)"
    print "Wins: " + str(team.wins)
    print "Losses: " + str(team.losses)
    print "Percentage: " + str(team.percentage)
    print ""

def game_by(team, teams):
    leader = teams[0]  
    return (float(leader.wins - team.wins + team.losses - leader.losses)/2.0)

def team_input():
    team_name = raw_input("Enter a team name: ")
    team_name = team_name.lower()
    if team_name in Team.team_names:
        return team_name
    team_names_shortened = []
    team_hash = {}
    for team in Team.team_names:
        team_names_shortened.append(team.split()[-1].lower())
        team_hash[team.split()[-1].lower()] = team

    while team_name not in Team.team_names and team_name not in team_names_shortened:
        team_name = raw_input("Unrecognized Input. Try again: ")

    if team_name in team_names_shortened:
        team_name = team_hash[team_name]

    return team_name

def recent_games():
    today_str = scraper.today()
    all_games = scraper.process_calendar() 
    games_today = [game for game in all_games if game['Date'] == today_str]

    if len(games_today) == 0:
        print "There are no games today"
    else:
        print "There are " + str(len(games_today)) + " games today:\n"
        for game in games_today:
            print "%s vs %s" % (game['W'], game['L'])

def menu():
    print "\n\n\n\n\n\nWelcome to the nba scraper! Below are your options:\n\n"
    print "1. Today's Games"
    print "2. Standings"
    print "3. Team Info"
    print "4. Quit"
    user_input = ""
    while not bool(re.compile('[1-4]').match(user_input)):
        user_input = raw_input("What do you want to see? (1-4): ")
    print "\n\n\n"
    return user_input

def games_today(teams = {}):
    recent_games()

def print_standings(teams = {}):
    east = east_teams(teams)
    west = west_teams(teams)
    print "\n\nEast Standings: "
    for team in east:
        print "%d. %s" % (team.seed, team.name) 

    print "\n\nWest standings: "
    for team in west:
        print "%d. %s" % (team.seed, team.name) 

def team_info(teams = {}):
    user_input = team_input()
    this_team = teams[user_input]
    summarize_team(this_team)

def stop(teams = {}):
    quit()

def run():
    teams = initialize_teams()
    options = { '1': games_today,
        '2': print_standings,
        '3': team_info,
        '4': stop
        }
    
    while True:
        user_input = menu()
        options[user_input](teams)



if __name__ == "__main__":
    """
    teams = initialize_teams()
    summarize_teams(west_teams(teams))
    summarize_teams(east_teams(teams))
    user_input = validate_input()
    this_team = teams[user_input]
    summarize_team(this_team)
    """
    run()

import scraper
from team import Team

def initialize_teams():
    teams = {}
    i = 0
    team_records = scraper.all_wins_losses()

    for team_name in Team.team_names:
        # print "Processing: " + team_name
        teams[team_name] = (Team(team_name, Team.divisions[i/5], team_records[team_name]))
    return teams 
 

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

    all_teams = {}
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

    for team in east_teams:
        team.set_seed(i)
        i += 1
    
    all_teams['E'] = east_teams
    all_teams['W'] = west_teams
    return all_teams
    
def summarize_teams(teams):
    for team in teams:
        summarize_team(team)

def summarize_team(team):
    print team.name + ": "
    print "Division: " + team.division
    print "Wins: " + str(team.wins)
    print "Losses: " + str(team.losses)
    print "Percentage: " + str(team.percentage)
    print ""


def game_by(team, teams):
    leader = teams[0]  
    return (float(leader.wins - team.wins + team.losses - leader.losses)/2.0)

def validate_input():
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

if __name__ == "__main__":
#def running_test():
    teams = initialize_teams()
    all_teams = order_teams(teams)
    west_teams = all_teams['W']
    east_teams = all_teams['E']
    user_input = validate_input()
    this_team = teams[user_input]
    summarize_team(this_team)

#if __name__ == "__main__":
#    validate_input()

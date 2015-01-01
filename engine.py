import scraper
from team import Team

def printstats(stats = {}):
    for key, value in stats.iteritems():
        print key, value

if __name__ == "__main__":
#def first_test():
    teams = []
    i = 0
    for team_name in Team.team_names:
        print "Processing: " + team_name
        teams.append(Team(team_name, Team.divisions[i/5], scraper.stats(team_name) + scraper.team_stats(team_name), []))
        i += 1
   
    print ""

    temp = teams[0]
    for team in teams:                          #testing that the teams were initialized correctly..
        print team.name + ":"
        print "Division: " + team.division
        print "Stats: " 
        printstats(team.stats)
        if temp > team:
            print team.name + " are behind " + temp.name + " in standings"
        temp = team
        print ""
        
#if __name__ == "__main__":
def single_test():
    this_team_name = Team.team_names[0]
    print "Processing: " + this_team_name
    this_team = Team(this_team_name, Team.divisions[0], scraper.stats(this_team_name) + scraper.team_stats(this_team_name), []) 
    print "Division: " + this_team.division
    print "Stats: "
    printstats(this_team.stats)
    printstats(this_team.pstats)

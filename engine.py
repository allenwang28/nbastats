import scraper
from team import Team

def printstats(stats = {}):
    for key, value in stats.iteritems():
        print key, value

if __name__ == "__main__":
    teams = []
    i = 0
    for team_name in scraper.team_names():
        print "Processing: " + team_name
        teams.append(Team(team_name, Team.divisions[i/5], scraper.stats(team_name), []))
        i += 1
   
    print ""

    for team in teams:
        print team.name + ":"
        print "Division: " + team.division
        print "Stats: " 
        printstats(team.stats)
        print ""
        


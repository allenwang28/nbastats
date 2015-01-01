from player import Player
team_stats_list = [ "Wins", "Losses", "Win/Loss %", "Game By", "Points scored per game", "Points allowed per game", "Simple Rating System" ]
player_stats_list = [ "G", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS", "PTS/G"  ]
all_team_stats = team_stats_list + player_stats_list



class Team:
    east_conference = [ "Atlantic", "Central", "Southeast" ]
    west_conference = [ "Northwest", "Pacific", "Southwest" ]
    divisions = east_conference + west_conference
    team_names = [u'Toronto Raptors', u'Brooklyn Nets', u'Boston Celtics', u'New York Knicks', u'Philadelphia 76ers', u'Chicago Bulls', u'Cleveland Cavaliers', u'Milwaukee Bucks', u'Indiana Pacers', u'Detroit Pistons', u'Atlanta Hawks', u'Washington Wizards', u'Miami Heat', u'Orlando Magic', u'Charlotte Hornets', u'Portland Trail Blazers', u'Oklahoma City Thunder', u'Denver Nuggets', u'Utah Jazz', u'Minnesota Timberwolves', u'Golden State Warriors', u'Los Angeles Clippers', u'Phoenix Suns', u'Sacramento Kings', u'Los Angeles Lakers', u'Memphis Grizzlies', u'Houston Rockets', u'Dallas Mavericks', u'San Antonio Spurs', u'New Orleans Pelicans']

    # REMINDER: stats are going to be represented in the form of strings!

    def __init__(self, n, d, team_stat_values = [], list_of_players = []):
        self.name = n
        self.division = d
        self.stats = dict(zip(all_team_stats, team_stat_values))
        self.players = list_of_players

    def conference(self):
        return "East" if division in east_conference else "West"
    
    def __cmp__(self, other):
        if float(self.stats[team_stats_list[2]]) < float(other.stats[team_stats_list[2]]):
            return -1
        if float(self.stats[team_stats_list[2]]) > float(other.stats[team_stats_list[2]]):
            return 1
        else:
            return 0

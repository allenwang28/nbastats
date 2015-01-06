class Team:
    east_conference = [ "Atlantic", "Central", "Southeast" ]
    west_conference = [ "Northwest", "Pacific", "Southwest" ]
    divisions = east_conference + west_conference
    team_names = [u'Toronto Raptors', u'Brooklyn Nets', u'Boston Celtics', u'New York Knicks', u'Philadelphia 76ers', u'Chicago Bulls', u'Cleveland Cavaliers', u'Milwaukee Bucks', u'Indiana Pacers', u'Detroit Pistons', u'Atlanta Hawks', u'Washington Wizards', u'Miami Heat', u'Orlando Magic', u'Charlotte Hornets', u'Portland Trail Blazers', u'Oklahoma City Thunder', u'Denver Nuggets', u'Utah Jazz', u'Minnesota Timberwolves', u'Golden State Warriors', u'Los Angeles Clippers', u'Phoenix Suns', u'Sacramento Kings', u'Los Angeles Lakers', u'Memphis Grizzlies', u'Houston Rockets', u'Dallas Mavericks', u'San Antonio Spurs', u'New Orleans Pelicans']
    
    def __init__(self, n, d, r = {}):
        self.name = n
        self.division = d
        self.wins = r['W']
        self.losses = r['L']
        self.percentage = r['%']
        self.vs = {}  

    def vs(self, other_team_name, w_l = []):
        self.vs[other_team_name] = w_l;

    def conference(self):
        return "East" if self.division in Team.east_conference else "West"
  
    def set_seed(self, seed):
        self.seed = seed

    def __cmp__(self, other):
        if self.percentage < other.percentage:
            return -1
        elif self.percentage == other.percentage:
            return 0
        else:
            return 1

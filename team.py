class Team:
    stats = [ "Wins", "Losses", "Win/Loss %", "Game By", "Points scored per game", "Points allowed per game", "Simple Rating System" ]
    east_conference = [ "Atlantic", "Central", "Southeast" ]
    west_conference = [ "Northwest", "Pacific", "Southwest" ]
    divisions = east_conference + west_conference

    # REMINDER: stats are going to be represented in the form of strings!

    def __init__(self, n, d, stat_values = [], p = []):
        self.name = n
        self.division = d
        self.stats = dict(zip(Team.stats, stat_values))

        self.players = p

    def conference(self):
        return "East" if division in east_conference else "West"



if __name__ == "__main__":
    Mavericks = Team("Mavericks", "Southwest", [ 23, 10, .697, 1.0, 109.6, 102.7, 6.24 ])
    print Mavericks.stats

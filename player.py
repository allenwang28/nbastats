
player_stats_list = [ "G", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS", "PTS/G" ]

class Player:
    def __initialize__(self, player_stat_values = []):
        self.stats = dict(zip(player_stats_list, player_stat_values))
          
        





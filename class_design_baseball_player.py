# BASEBALLPLAYER

# A baseball player has a name and a jersey number. Most players hit either right or left, but some can hit 
# either way. This object should be able to react when a player completes a game, recording how many 
# hits and RBIs the player earned in that game. A player has a certain number of runs and RBIs he or she 
# has recorded over all games played. A player has a certain number of games he or she has played.

class BaseballPlayer:

    def __init__(self, name, jersey_num):
        """Create a new baseball player with the given name and jersey number."""
        self.name = name
        self.jersey_num = jersey_num
        self.ambidextrous = False
        self.total_hits = 0
        self.total_runs = 0
        self.total_RBIs = 0
        self.games_played = 0
        self.game_stats = {}
    
    def __repr__(self):
        return self.name + " - Jersey #" + str(self.jersey_num)

    def get_name(self):
        return self.name

    def get_jersey_num(self):
        return self.jersey_num

    def is_ambidextrous(self):
        self.ambidextrous = True
    
    def add_stats(self, game_hits, game_RBIs, game_runs=None):
        self.games_played += 1
        self.game_stats[self.games_played] = (game_hits, game_RBIs, game_runs)
        self.total_hits += game_hits
        self.total_RBIs += game_RBIs
        if game_runs != None:
            self.total_runs += game_runs

def main():
    eric_hosmer = BaseballPlayer("Eric Hosmer", 35)
    print(eric_hosmer)
    print("Player's name:", eric_hosmer.get_name())
    print("Player's jersey number:" + str(eric_hosmer.get_jersey_num()))
    print("Player is ambidextrous?", eric_hosmer.ambidextrous)
    eric_hosmer.is_ambidextrous()
    print("Player is ambidextrous?",eric_hosmer.ambidextrous)
    print(eric_hosmer.get_name()  + "'s game stats are:" + str(eric_hosmer.game_stats))
    eric_hosmer.add_stats(5, 2)
    print("After the first game, " + eric_hosmer.get_name()  + "'s game stats were:" + str(eric_hosmer.game_stats))
    eric_hosmer.add_stats(3, 2, 2)
    print("After the second game, " + eric_hosmer.get_name()  + "'s game stats were:" + str(eric_hosmer.game_stats))
    eric_hosmer.add_stats(2, 1, 1)
    print("These were the stats for his third game: ", str(eric_hosmer.game_stats[3]))
    print(eric_hosmer.get_name(), "has been in", eric_hosmer.games_played, "games.")

if __name__ == "__main__":
    main()
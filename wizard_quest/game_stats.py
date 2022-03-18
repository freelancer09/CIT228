class GameStats:

    def __init__(self, wq_game):
        self.settings = wq_game.settings
        self.reset_stats()

        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        self.score = 0
        self.level = 1
        self.lives_left = 3
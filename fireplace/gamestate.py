class GameState:

    def __init__(self, game):
        self.game = game
        self.ally = game.player1
        self.enemy = game.player2
        self.enemy_targets = []
        self.ally_characters = []

    def set_health(self, player):
        pass

    def set_target_list(self):
        return self.enemy_targets

    def update(self, game):
        self.game = game
        self.enemy_targets = self.ally.characters[0].targets
        print("TARGETS: {}".format(self.enemy_targets))

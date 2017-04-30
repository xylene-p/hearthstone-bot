class GameState:

    def __init__(self, game):
        self.game = game
        if game.player1.name is "Player":
            self.ally = game.player1
            self.enemy = game.player2
        else:
            self.ally = game.player2
            self.enemy = game.player1
        self.enemy_targets = []
        self.ally_characters = []
        self.enemy_hero_health = 30
        self.ally_hero_health = 30
        self.ally_total_attack = 0
        self.ally_total_health = 0
        self.enemy_total_attack = 0
        self.enemy_total_health = 0
        self.total_number_of_turns = 0

    def update(self, game):
        self.game = game
        self.enemy_targets = self.ally.characters[0].targets
        self.ally_characters = self.ally.characters
        self.enemy_hero_health = self.enemy.hero.health
        self.ally_hero_health = self.ally.hero.health
        self.update_total_attack_health()
        self.total_number_of_turns = game.turn
        # print("");
        # print("TARGETS: {}".format(self.enemy_targets))
        # print("ALLIES: {}".format(self.ally_characters))
        # print("ENEMY HERO HEALTH: {}".format(self.enemy_hero_health))
        # print("HERO HEALTH: {}".format(self.ally_hero_health))
        # print("TOTAL ALLY ATTACK: {}".format(self.ally_total_attack))
        # print("TOTAL ALLY HEALTH: {}".format(self.ally_total_health))
        # print("TOTAL ENEMY ATTACK: {}".format(self.enemy_total_attack))
        # print("TOTAL ENEMY HEALTH: {}".format(self.enemy_total_health))
        # print("TOTAL NUMBER OF TURNS {}".format(self.total_number_of_turns))
        # print("");

    def update_total_attack_health(self):
        # Update ally total attack and health
        total_attack = 0
        total_health = 0
        for character in self.ally_characters:
            total_attack += character.atk
            total_health += character.health
        self.ally_total_attack = total_attack
        self.ally_total_health = total_health

        # Update enemy total attack and health
        total_attack = 0
        total_health = 0
        for target in self.enemy_targets:
            total_attack += target.atk
            total_health += target.health
        self.enemy_total_attack = total_attack
        self.enemy_total_health = total_health

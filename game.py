import random

class Player:
    def __init__(self, name):
        self.name = name
        self.role = None
        self.alive = True

class WerewolfGame:
    def __init__(self, players):
        self.players = [Player(name) for name in players]
        self.roles = ['Werewolf', 'Villager', 'Seer', 'Bodyguard']
        self.assign_roles()
        
    def assign_roles(self):
        roles = self.roles.copy()
        if len(self.players) > len(roles):
            roles += ['Villager'] * (len(self.players) - len(roles))
        random.shuffle(roles)
        for player, role in zip(self.players, roles):
            player.role = role
            
    def night_phase(self):
        print("Night falls...")
        werewolves = [player for player in self.players if player.role == 'Werewolf' and player.alive]
        if werewolves:
            target = random.choice([player for player in self.players if player.alive and player.role != 'Werewolf'])
            target.alive = False
            print(f"{target.name} was killed by the werewolves!")
        
    def day_phase(self):
        print("Day breaks...")
        alive_players = [player for player in self.players if player.alive]
        if not alive_players:
            print("No one is left alive.")
            return
        print("Players who are still alive:")
        for player in alive_players:
            print(player.name)
        vote = random.choice(alive_players)
        vote.alive = False
        print(f"{vote.name} was voted out by the villagers!")
        
    def check_win_condition(self):
        werewolves = [player for player in self.players if player.role == 'Werewolf' and player.alive]
        villagers = [player for player in self.players if player.role != 'Werewolf' and player.alive]
        if not werewolves:
            print("Villagers win!")
            return True
        if len(werewolves) >= len(villagers):
            print("Werewolves win!")
            return True
        return False
        
    def play_game(self):
        while True:
            self.night_phase()
            if self.check_win_condition():
                break
            self.day_phase()
            if self.check_win_condition():
                break

# Example usage
players = ["Alice", "Bob", "Charlie", "David"]
game = WerewolfGame(players)
game.play_game()


class Player:
    def __init__(self):
        self.player_health = 100
        self.MAX_ITEMS = 8
        self.available_items = [None for _ in range(self.MAX_ITEMS)]

    def subtractHealth(self, amount):
        self.player_health -= amount
    
    def isAlive(self):
        return self.player_health > 0

    def heal(self, amount):
        self.player_health = min(100, self.player_health + amount)


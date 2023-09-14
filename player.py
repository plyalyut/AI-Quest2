
class Player:
    def __init__(self):
        self.player_health = 100
        self.MAX_ITEMS = 8
        self.available_items = []

    def subtractHealth(self, amount):
        self.player_health -= int(amount)
    
    def isAlive(self):
        return self.player_health > 0

    def heal(self, amount):
        self.player_health = min(100, self.player_health + amount)

    def add_item(self, item):
        if len(self.available_items) >= self.MAX_ITEMS:
            return
        else:
            self.available_items.append(item)
    
    def remove_item(self, item):
        if item in self.available_items:
            self.available_items.remove(item)
        else:
            return
    
    def get_items(self):
        return self.available_items


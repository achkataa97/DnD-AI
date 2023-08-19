class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
    
    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]
    
    def get_items(self):
        return self.items

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    
    def attack(self, attacker, defender):
        # This is a basic attack logic; you can expand it with skills, magic, etc.
        damage = 10  # fixed damage for now
        defender['health'] -= damage
        return f"{attacker['name']} attacked {defender['name']} for {damage} damage!"

    def player_attack(self):
        return self.attack(self.player, self.enemy)
    
    def enemy_attack(self):
        return self.attack(self.enemy, self.player)

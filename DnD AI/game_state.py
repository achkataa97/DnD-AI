class GameState: 
    def __init__(self): 
        self.character = { 
            'name': '', 
            'gender': '', 
            'class': '', 
            'race': '', 
            'abilities': [], 
            'skills': [], 
            'equipment': [], 
            'health': 100, 
            'mana': 100, 
            'inventory': [], 
            'gold': 50 
        }
        self.reputation = 0  # -100 (worst) to 100 (best)
        self.morality = 0  # -100 (evil) to 100 (good)
        self.relationships = {}  # E.g., {'John': 'friend', 'Sara': 'enemy'}
        self.quests = { 
            'active': [], 
            'completed': [] 
        }
        self.allies = [] 
        self.enemies = [] 
        self.locations_visited = [] 
        self.decisions = [] 
        self.npc_attitudes = {} 
        self.environment_states = { 
            'town': 'neutral',   # Can be 'flourishing', 'decaying', etc. 
        }
        self.player_performance = 'average'  # Can be 'good', 'bad', 'average'
 
    def update_health(self, change): 
        self.character['health'] += change 
        self.character['health'] = min(100, max(0, self.character['health'])) 

    def update_mana(self, change): 
        self.character['mana'] += change 
        self.character['mana'] = min(100, max(0, self.character['mana'])) 

    def modify_gold(self, change): 
        self.character['gold'] += change 

    def add_item(self, item): 
        self.character['inventory'].append(item) 

    def remove_item(self, item): 
        self.character['inventory'].remove(item) 

    def add_quest(self, quest): 
        self.quests['active'].append(quest) 

    def complete_quest(self, quest): 
        self.quests['active'].remove(quest) 
        self.quests['completed'].append(quest) 

    def add_ally(self, ally): 
        self.allies.append(ally) 

    def add_enemy(self, enemy): 
        self.enemies.append(enemy) 

    def visit_location(self, location): 
        self.locations_visited.append(location) 

    def make_decision(self, decision): 
        self.decisions.append(decision) 

    def set_npc_attitude(self, npc, attitude): 
        self.npc_attitudes[npc] = attitude 

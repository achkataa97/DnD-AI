import sqlite3

class SaveLoadSystem:
    def __init__(self, db_path='game.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def save_game(self, player_data, game_state_data):
        # Insert or update player data
        self.cursor.execute('''
            REPLACE INTO players (id, name, health, gold, reputation, morality)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (player_data['id'], player_data['name'], player_data['health'], player_data['gold'], player_data['reputation'], player_data['morality']))

        # Insert or update game state data
        self.cursor.execute('''
            REPLACE INTO game_states (id, player_id, location, quest, npc_relationship)
            VALUES (?, ?, ?, ?, ?)
        ''', (game_state_data['id'], game_state_data['player_id'], game_state_data['location'], game_state_data['quest'], game_state_data['npc_relationship']))

        self.conn.commit()

    def load_game(self, player_id):
        # Retrieve player data
        self.cursor.execute('SELECT * FROM players WHERE id=?', (player_id,))
        player_data = self.cursor.fetchone()

        # Retrieve game state data for the player
        self.cursor.execute('SELECT * FROM game_states WHERE player_id=?', (player_id,))
        game_state_data = self.cursor.fetchone()

        return player_data, game_state_data

    def close(self):
        self.conn.close()

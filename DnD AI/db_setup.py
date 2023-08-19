import sqlite3

def setup_database(): 
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()

    # Players table
    cursor.execute('''CREATE TABLE IF NOT EXISTS players 
                     (id INTEGER PRIMARY KEY, 
                      name TEXT, 
                      health INTEGER, 
                      gold INTEGER, 
                      reputation INTEGER, 
                      morality INTEGER)''')

    # Game states table
    cursor.execute('''CREATE TABLE IF NOT EXISTS game_states 
                     (id INTEGER PRIMARY KEY, 
                      player_id INTEGER, 
                      location TEXT, 
                      quest TEXT, 
                      npc_relationship TEXT)''')

    # NPC table
    cursor.execute('''CREATE TABLE IF NOT EXISTS npcs 
                     (id INTEGER PRIMARY KEY, 
                      name TEXT, 
                      attitude TEXT, 
                      backstory TEXT)''')

    # World lore table
    cursor.execute('''CREATE TABLE IF NOT EXISTS world_lore 
                     (id INTEGER PRIMARY KEY, 
                      event_name TEXT, 
                      event_description TEXT)''')

    conn.commit()
    conn.close()

setup_database()

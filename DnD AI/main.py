from gpt2_interaction import load_model, generate_story, create_character, generate_world 
from game_state import GameState 
from command_parser import parse_command 
from npc_interaction import NPC
from error_handler import validate_response

def play_game(): 
    model, tokenizer = load_model() 
    game_state = GameState()
    active_npcs = {}  # Keep track of NPCs we've interacted with to maintain continuity

    print("Welcome to AI DnD!") 
    character = create_character(model, tokenizer) 

    while True: 
        print("\nYour character sheet:") 
        for key, value in character.items(): 
            print(f"{key}: {value}") 

        confirmation = input("\nAre you sure with your choices? (Yes/No): ").lower() 
        if confirmation == 'yes': 
            break 
        elif confirmation == 'no': 
            character = create_character(model, tokenizer) 

    world_description = generate_world(model, tokenizer) 
    print(f"\n{world_description}") 
    print("\nYou find yourself in this mystical land. What would you like to do?") 

    while True: 
        user_input = input("Enter your command: ") 

        if 'talk to' in user_input:
            npc_name = user_input.split('talk to ')[1]  # Extracting NPC name from input
            if npc_name not in active_npcs:
                active_npcs[npc_name] = NPC(npc_name)
            response = active_npcs[npc_name].interact(user_input)
        else:
            action = parse_command(user_input) 
            context = f"Given the world state as {vars(game_state)}, player's performance being {game_state.player_performance}, and player's intention to {action}, " + user_input 
            generated_story, game_state = generate_story(model, tokenizer, context, game_state) 
            response = validate_response(generated_story, game_state)  # Check the AI response for inconsistencies

        print(response) 

        if "you died" in response: 
            print("Game Over!") 
            break 

        if "you win" in response: 
            print("Congratulations, you have won the game!") 
            break 

if __name__ == "__main__": 
    play_game()

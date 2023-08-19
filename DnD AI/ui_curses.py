import curses
from gpt2_interaction import load_model, generate_story
from game_state import GameState
from command_parser import parse_command

model, tokenizer = load_model()
game_state = GameState()
previous_interactions = []

def game_ui(screen): 
    # Initialize window 
    curses.start_color() 
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK) 
    screen.bkgd(curses.color_pair(1))
    curses.curs_set(0)

    # Print the welcome message 
    screen.addstr("Welcome to AI DnD!\n", curses.A_BOLD)

    # Input loop
    while True: 
        screen.addstr("\nEnter your command: ")

        # Get user input
        user_input = screen.getstr().decode('utf-8')

        if user_input == "exit": 
            break

        # Pass user_input to game logic, get the response, and display it
        context = f"Given the world state as {vars(game_state)}, player's performance being {game_state.player_performance}, and player's intention as: {user_input}"
        generated_story, game_state = generate_story(model, tokenizer, context, game_state)
        previous_interactions.append(generated_story)
        screen.addstr("\n" + generated_story)

        if "you died" in generated_story:
            screen.addstr("\nGame Over!")
            break

        if "you win" in generated_story:
            screen.addstr("\nCongratulations, you have won the game!")
            break

curses.wrapper(game_ui)

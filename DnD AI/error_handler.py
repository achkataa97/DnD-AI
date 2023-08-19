import re

def validate_response(response, game_state):
    """
    Validate the AI generated response for any contradictions with the game state.
    If any inconsistencies are found, a general error message is returned.
    """
    
    # Example of a simple validation: Check if AI mentions a quest completion that isn't in active quests.
    completed_quest = re.search(r"you have completed the quest: ([\w\s]+)", response, re.I)
    if completed_quest:
        quest_name = completed_quest.group(1)
        if quest_name not in game_state.quests['active']:
            return f"You can't complete the quest '{quest_name}' as it's not in your active quests!"

    # Other validation checks can be added here based on game lore, character state, etc.
    
    return response

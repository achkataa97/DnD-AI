from transformers import GPT2LMHeadModel, GPT2Tokenizer
from game_state import GameState

def load_model(): 
    model_name = 'gpt2-medium' 
    model = GPT2LMHeadModel.from_pretrained(model_name) 
    tokenizer = GPT2Tokenizer.from_pretrained(model_name) 
    return model, tokenizer

def generate_story(model, tokenizer, prompt, game_state, max_length=1000, temperature=0.7): 
    input_ids = tokenizer.encode(prompt, return_tensors='pt') 
    output = model.generate(input_ids, max_length=max_length, temperature=temperature, pad_token_id=tokenizer.eos_token_id, no_repeat_ngram_size=2) 
    story = tokenizer.decode(output[0], skip_special_tokens=True)
    updated_game_state = update_world_state(story, game_state)
    return story, updated_game_state

def create_character(model, tokenizer): 
    prompt = "Describe a character in a fantasy world with attributes like name, gender, class, race, abilities, skills, and starting equipment." 
    character_description = generate_story(model, tokenizer, prompt, None, max_length=150)[0] 
    character_attributes = character_description.split(", ")
    character = {}
    for attr in character_attributes: 
        key, value = attr.split(": ")
        character[key] = value
    return character

def generate_world(model, tokenizer, custom_prompt): 
    world_description = generate_story(model, tokenizer, custom_prompt, None, max_length=300)[0] 
    return world_description

def update_world_state(response, game_state):
    # This function should be expanded to handle other aspects of the world state
    if "quest:" in response: 
        quest_name = response.split("quest:")[1].split(".")[0].strip() 
        game_state.add_quest(quest_name)
    return game_state

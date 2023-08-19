from gpt2_interaction import load_model, generate_story

class NPC:
    def __init__(self, name):
        self.name = name
        self.model, self.tokenizer = load_model()
        self.generate_details()

    def generate_details(self):
        prompt = f"Describe the backstory, personality, and motivations of {self.name}."
        description = generate_story(self.model, self.tokenizer, prompt, None, max_length=300)[0]
        
        details = description.split(", ")
        self.details = {}
        for detail in details:
            key, value = detail.split(": ")
            self.details[key] = value

    def interact(self, player_input):
        prompt = f"{self.name} responds to {player_input} considering that {self.details['backstory']} and being {self.details['personality']}."
        response = generate_story(self.model, self.tokenizer, prompt, None, max_length=300)[0]
        return response

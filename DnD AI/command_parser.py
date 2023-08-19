def parse_command(command): 
    command = command.lower() 
    if 'attack' in command: 
        return 'combat' 
    elif 'trade' in command or 'buy' in command or 'sell' in command: 
        return 'trade' 
    elif 'talk' in command or 'speak' in command: 
        return 'dialogue' 
    elif 'use' in command: 
        return 'use_item'
    elif 'learn' in command or 'train' in command:
        return 'training'
    else: 
        return 'explore'

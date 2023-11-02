def roll_call_dwarves(dwarf_list):
    for i in range(0, len(dwarf_list)):
        print(f"{i + 1}. {dwarf_list[i]}")

def summon_captain_planet(planeteer_calls):
    return [call.title() + "!" for call in planeteer_calls]

def long_planeteer_calls(word_list):
    for word in word_list:
        if len(word) > 4:
            return True
    
    return False

def find_the_cheese(word_list):
    cheese_list = ["cheddar", "gouda", "camembert"]
    for word in word_list:
        if word in cheese_list:
            return word

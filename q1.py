import random

def spin_twister_spinner():
    """
    Returns a list with a random color, side, and appendage
    
    colors: "red", "green", "yellow", or "blue"
    sides: "left" or "right"
    appendage: "hand" or "foot"
    """
    colors = ["red", "green", "yellow", "blue"]
    sides = ["left", "right"]
    appendages = ["hand", "foot"]
    
    # Randomly select one element from each list
    color = random.choice(colors)
    side = random.choice(sides)
    appendage = random.choice(appendages)
    
    return [color, side, appendage]

# Here's the function call. This should print a random assortment of twister commands
for _ in range(10):
    print(spin_twister_spinner())
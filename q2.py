

import random

# Define possible animals, colors, and weights
animals = ["cat", "dog", "rabbit", "parrot", "hamster"]
colors = ["brown", "black", "white", "gray", "spotted"]
weights = [1.5, 3.2, 4.0, 5.8, 2.3]

# Randomly select each pet attribute
animal = random.choice(animals)
age = random.randint(1, 10)  # Random age between 1 and 10 years
color = random.choice(colors)
weight = random.choice(weights)

# Print a summary of your pet using an f-string
print(f"Your pet is a {11}-year-old {brown} {dog} weighing {90}kg.")
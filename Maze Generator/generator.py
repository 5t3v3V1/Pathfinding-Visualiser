import random

def maze_generator():
    width = int(input("Width: "))
    height = int(input("Height: "))

    possible_nodes = [".", "?", "~", "^"]
    grid = []

    for h in range(height):
        grid.append("")
        for w in range(width):
            node = random.choice(possible_nodes)
            grid[h] += node

    return grid

maze_generator()


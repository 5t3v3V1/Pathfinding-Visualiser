# Pathfinding Algorithm Visualiser

## What is it

This repo contains my algorithm visualiser containing my BFS, DFS, Dijkstra's and A* algorithm. It also includes it's maze generator capable of different levelled terrains.

## Algorithms Implemented

Grid Generator
Allows the user to input the desired width and height of the grid they want to generate, then lays out the possible nodes and the proabbilities they 
have of showing up before, creating the an array called grid, which is where the layout will live, and creates a new string "" the number of times there is height and
for each string appends a random node type the width number of times, before returning the finished layout.

BFS
Creates a queue containing the start position, it then pops out the first index of the queue, checks whether its the end position, if not it finds all of it's neighbours,
adds them to the queue if they havent already been visited, and repeats until the end position is reached.

DFS
Operates very similar, in the case it does the exact same checks, but instead of a queue, it uses a stack, meaning when instead of popping the first index of the array it pops the last.

Dijkstra
Continiously picks out the node with the smallest cost, removes node from a copy of dicitonary containing all psoitions and their costs, finds the neigbhbours, assigns
new costs by using the nieghbour's weight, and then repeat until end node is reached.

A*
Similar to Dijkstra's but picks out the node with the smallest total cost, containing their cost and the cost to the end, removes node from a copy of the dictionary
containing all positions and their costs, finds the neighbours, assigns the number a new total cost by finding its cost to the end aswell as the cost to get to it, and 
then repeats until the end node is reached

## How to Run

**Requirements:** Python 3.8+

```bash
git clone https://github.com/5t3v3V1/Pathfinding-Visualiser
cd Pathfinding-Visualiser
python visualiser.py
```

## Screenshot

<img width="136" height="214" alt="image" src="https://github.com/user-attachments/assets/d025c697-4d1a-46cb-b50e-2a2bc560e466" />
<img width="894" height="281" alt="image" src="https://github.com/user-attachments/assets/2be992e1-c315-466f-b23d-f27703ba7cb9" />


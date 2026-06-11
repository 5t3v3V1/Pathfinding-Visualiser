
class Grid:
    def __init__(self, layout):
        self.layout = layout.copy()
        self.nodes = {}
        self.reset_layout = layout.copy()
    
    def visualise_grid(self):
        for row in self.layout:
            for node in row:
                if node.path:
                    print("*", end = "")
                elif node.visited or node.type == "visited_node":
                    print("!", end = "")
                elif node.type == "wall":
                    print("#", end = "")
                elif node.weight == 1:
                    print(".", end = "")
                elif node.weight == 5:
                    print("?", end = "")
                elif node.weight == 10:
                    print("~", end = "")
                elif node.weight == 15:
                    print("^", end = "")
            print()

    def append_nodes(self):
        for row_index, row in enumerate(self.layout):
            row_items = list(row)
            for index, item in enumerate(row_items):
                if item == "#":
                    node = Node("wall", (index, row_index), 0, False)
                    self.nodes[(index, row_index)] = node
                    row_items[index] = node
                    self.layout[row_index] = row_items
                elif item == ".":
                    node = Node("node", (index, row_index), 1, False)
                    self.nodes[(index, row_index)] = node
                    row_items[index] = node
                    self.layout[row_index] = row_items
                elif item == "?":
                    node = Node("node", (index, row_index), 5, False)
                    self.nodes[(index, row_index)] = node
                    row_items[index] = node
                    self.layout[row_index] = row_items
                elif item == "~":
                    node = Node("node", (index, row_index), 10, False)
                    self.nodes[(index, row_index)] = node
                    row_items[index] = node
                    self.layout[row_index] = row_items
                elif item == "^":
                    node = Node("node", (index, row_index), 15, False)
                    self.nodes[(index, row_index)] = node
                    row_items[index] = node
                    self.layout[row_index] = row_items

        return self.layout         
    
    def reset(self):
        self.layout = self.reset_layout.copy()
        self.nodes = {}


class Node:
    def __init__(self, type, position, weight, visited):
        self.type = type
        self.position = position
        self.visited = visited
        self.weight = weight
        self.parent = None
        self.path = False
        self.cost = float("inf")
        self.cost_to_end = 0
        self.total_cost = float("inf")

    def get_neighbours(self):
        x, y = self.position
        return [(x, y - 1),
                (x - 1, y),
                (x, y + 1),
                (x + 1, y)
                ]
    
    def visit(self):
        self.visited = True
        self.type = "visited_node"
    
    def pathed(self):
        self.path = True




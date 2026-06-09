
class Grid:
    def __init__(self, layout):
        self.layout = layout
        self.nodes = {}
    
    def visualise_grid(self):
        for row in self.layout:
            for node in row:
                if node.path:
                    print("*", end = "")
                elif node.visited or node.type == "visited_node":
                    print("!", end = "")
                elif node.type == "wall":
                    print("#", end = "")
                elif not node.visited:
                    print("?", end = "")
            print()

    def append_nodes(self):
        for row_index, row in enumerate(self.layout):
            row_items = list(row)
            for index, item in enumerate(row_items):
                if item == "#":
                    node = Node("wall", (index, row_index), False)
                    self.nodes[(index, row_index)] = node
                    row_items[index] = node
                    self.layout[row_index] = row_items
                elif item == "?":
                    node = Node("node", (index, row_index), False)
                    self.nodes[(index, row_index)] = node
                    row_items[index] = node
                    self.layout[row_index] = row_items

        return self.layout
    
    def run(self):
        self.append_nodes()
        self.visualise_grid()
            

class Node:
    def __init__(self, type, position, visited):
        self.type = type
        self.position = position
        self.visited = visited
        self.parent = None
        self.path = False

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




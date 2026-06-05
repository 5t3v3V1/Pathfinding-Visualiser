
class Grid:
    def __init__(self, layout):
        self.layout = layout
    
    def visualise_grid(self):
        for row in self.layout:
            for node in row:
                if node.type == "node":
                    print(node.position, end = "")
                elif node.type == "wall":
                    print(node.position, end = "")
            print()

    def append_nodes(self):
        for row_index, row in enumerate(self.layout):
            row_items = list(row)
            for index, item in enumerate(row_items):
                if item == "#":
                    node = Node("wall", (index, row_index), False)
                    row_items[index] = node
                    self.layout[row_index] = row_items
                elif item == "?":
                    node = Node("node", (index, row_index), False)
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


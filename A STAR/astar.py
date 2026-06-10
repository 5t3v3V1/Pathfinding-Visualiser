from classes import Grid, Node

grid = Grid([
    "........",
    ".######.",
    ".#....#.",
    ".#....#.",
    ".######.",
    "........"
])
noded_grid = grid.append_nodes()

def identify_node(node_position):
    identified_node = grid.nodes.get(node_position)
    return identified_node

def astar(grid_with_nodes):
    grid.visualise_grid()
    for row in grid_with_nodes:
        for column in row:
            print(column.position, end = "")
        print()

    while True:
        try:
            start_position = tuple(input("Select start position: "))
            x, y = start_position
            m, n = int(x), int(y)
            start_position = (m, n)
            end_position = tuple(input("Select end position: "))
            l, o = end_position
            p, k = int(l), int(o)
            end_position = (p, k)

            start_node = identify_node(start_position)
            if start_node.type == "wall":
                print("Wall selected as start node, please reselect")
            else:
                break
        except ValueError:
            pass

    unvisited = set()
    visited = set()
    node_costs_global = {}
    start_node = identify_node(start_position)
    start_node.cost = 0
    start_node.total_cost = 0
    for row in grid_with_nodes:
        for column in row:
            node_costs_global[column.position] = column.total_cost
            unvisited.add(column.position)

    while unvisited:
        node_costs = node_costs_global.copy()

        for node in list(node_costs.items()):
            if node[0] in visited:
                node_costs.pop(node[0])

        min_cost = min(node_costs.values())

        current = 0

        for node in list(node_costs.items()):
            if node[1] == min_cost:
                current = node[0]

        current_node = identify_node(current)
        current_node.visit()
        grid.visualise_grid()
        print()

        if current == end_position:
            path = []

            node = current_node

            while node is not None:
                path.append(node.position)
                node.pathed()
                node = node.parent
    
            grid.visualise_grid()                
            print()
            print(node_costs_global)
            path.reverse()
            print(path)
            break

        for neighbour in current_node.get_neighbours():
            neighbour = identify_node(neighbour)
            if neighbour is None:
                continue
                
            new_cost = current_node.cost + neighbour.weight
            neighbour.cost_to_end = abs(neighbour.position[0] - end_position[0]) + abs(neighbour.position[1] - end_position[1])
            neighbour.total_cost = neighbour.cost_to_end + new_cost

            if neighbour.type != "wall":
                if new_cost < neighbour.cost:
                    neighbour.parent = current_node
                    neighbour.cost = new_cost
                    node_costs[neighbour.position] = neighbour.total_cost
                    node_costs_global[neighbour.position] = neighbour.total_cost

        unvisited.discard(current)
        visited.add(current)
                    

astar(noded_grid)
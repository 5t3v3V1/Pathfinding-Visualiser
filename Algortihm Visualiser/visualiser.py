from classes import Grid, Node

def identify_node(grid, node_position):
    identified_node = grid.nodes.get(node_position)
    return identified_node

def bfs(grid):
    grid.visualise_grid()
    grid_with_nodes = grid.append_nodes()
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

            start_node = identify_node(grid, start_position)
            if start_node.type == "wall":
                print("Wall selected as start node, please reselect")
            else:
                break
        except ValueError:
            pass

    queue = [start_position]
    visited = {start_position}
    visit_order = [start_position]
    nodes_visited = 0

    while queue:
        current = queue.pop(0)
        current_node = identify_node(grid, current)
        current_node.visit()
        nodes_visited += 1
        grid.visualise_grid()
        print()



        if current == end_position:
            path = []

            node = current_node

            while node is not None:
                path.append(node.position)
                node = node.parent

            path.reverse()

            for node_position in path:
                identified_node = identify_node(grid, node_position)
                identified_node.pathed()

            grid.visualise_grid()

            print(f"Order visited is: {visit_order}")
            print(f"Shortest_path is: {path}")
            print(f"Nodes Visited: {nodes_visited}")
            break

        for neighbour in current_node.get_neighbours():
            neighbour = identify_node(grid, neighbour)
            if neighbour is None:
                continue

            if neighbour.type != "wall":
                if neighbour.position not in visited:
                    neighbour.parent = current_node
                    neighbour.visit()
                    visited.add(neighbour.position)
                    visit_order.append(neighbour.position)
                    queue.append(neighbour.position)


def dfs(grid):
    grid.visualise_grid()
    grid_with_nodes = grid.append_nodes()
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

            start_node = identify_node(grid, start_position)
            if start_node.type == "wall":
                print("Wall selected as start node, please reselect")
            else:
                break
        except ValueError:
            pass

    stack = [start_position]
    visited = {start_position}
    visit_order = [start_position]
    nodes_visited = 0

    while stack:
        current = stack.pop()
        current_node = identify_node(grid, current)
        current_node.visit()
        nodes_visited += 1
        grid.visualise_grid()
        print()

        if current == end_position:
            
            path = []

            node = current_node

            while node is not None:
                path.append(node.position)
                node = node.parent

            path.reverse()

            for node_position in path:
                identified_node = identify_node(grid, node_position)
                identified_node.pathed()

            grid.visualise_grid()

            print(f"Order visited is: {visit_order}")
            print(f"Path is: {path}")
            print(f"Nodes Visited: {nodes_visited}")
           
            break
            

        for neighbour in current_node.get_neighbours():
            neighbour = identify_node(grid, neighbour)
            if neighbour is None:
                continue

            elif neighbour.type != "wall":
                if neighbour.position not in visited:
                    neighbour.parent = current_node
                    neighbour.visit()
                    visited.add(neighbour.position)
                    visit_order.append(neighbour.position)
                    stack.append(neighbour.position)

def dijkstra(grid):
    grid.visualise_grid()
    grid_with_nodes = grid.append_nodes()
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

            start_node = identify_node(grid, start_position)
            if start_node.type == "wall":
                print("Wall selected as start node, please reselect")
            else:
                break
        except ValueError:
            pass

    unvisited = set()
    visited = set()
    node_costs_global = {}
    nodes_visited = 0
    start_node = identify_node(grid, start_position)
    start_node.cost = 0
    for row in grid_with_nodes:
        for column in row:
            node_costs_global[column.position] = column.cost
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

        current_node = identify_node(grid, current)
        current_node.visit()
        nodes_visited += 1
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
            print(f"Shortest Path: {path}")
            print(f"Nodes Visited: {nodes_visited}")
            break

        for neighbour in current_node.get_neighbours():
            neighbour = identify_node(grid, neighbour)
            if neighbour is None:
                continue
                
            new_cost = current_node.cost + neighbour.weight

            if neighbour.type != "wall":
                if new_cost < neighbour.cost:
                    neighbour.parent = current_node
                    neighbour.visit()
                    neighbour.cost = new_cost
                    node_costs[neighbour.position] = neighbour.cost
                    node_costs_global[neighbour.position] = neighbour.cost

        unvisited.discard(current)
        visited.add(current)

def astar(grid):
    grid.visualise_grid()
    grid_with_nodes = grid.append_nodes()
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

            start_node = identify_node(grid, start_position)
            if start_node.type == "wall":
                print("Wall selected as start node, please reselect")
            else:
                break
        except ValueError:
            pass

    unvisited = set()
    visited = set()
    node_costs_global = {}
    nodes_visited = 0
    start_node = identify_node(grid, start_position)
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

        current_node = identify_node(grid, current)
        current_node.visit()
        nodes_visited += 1
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
            print(f"Shortest Path: {path}")
            print(f"Nodes Visited: {nodes_visited}")
            break

        for neighbour in current_node.get_neighbours():
            neighbour = identify_node(grid, neighbour)
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

def run():
    while True:
        grid = Grid([
            "????????",
            "????????",
            "????????",
            "????????",
            "????????"
        ])
        grid.append_nodes()
        grid.visualise_grid()
        print("1. BFS")
        print("2. DFS")
        print("3. Dijkstra")
        print("4. A*")
        print("5. Exit")

        choice = input("Choose Algorithm: ")

        if choice == "1":
            bfs(grid)

        elif choice == "2":
            dfs(grid)

        elif choice == "3":
            dijkstra(grid)

        elif choice == "4":
            astar(grid)

        elif choice == "5":
            break
    
        else:
            print("Invalid Choice")

run()
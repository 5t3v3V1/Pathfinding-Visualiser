from classes import Grid, Node

grid = Grid([
    "????????",
    "????????",
    "????????",
    "????????",
    "????????"
])
noded_grid = grid.append_nodes()

def identify_node(node_position):
    identified_node = grid.nodes.get(node_position)
    return identified_node

def bfs(grid_with_nodes):
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

    queue = [start_position]
    visited = {start_position}
    visit_order = [start_position]

    while queue:
        current = queue.pop(0)
        current_node = identify_node(current)
        current_node.visit()
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
                identified_node = identify_node(node_position)
                identified_node.pathed()

            grid.visualise_grid()

            print(f"Order visited is: {visit_order}")
            print(f"Shortest_path is: {path}")
            break

        for neighbour in current_node.get_neighbours():
            neighbour = identify_node(neighbour)
            if neighbour is None:
                continue

            if neighbour.type != "wall":
                if neighbour.position not in visited:
                    neighbour.parent = current_node
                    neighbour.visit()
                    visited.add(neighbour.position)
                    visit_order.append(neighbour.position)
                    queue.append(neighbour.position)



bfs(noded_grid)
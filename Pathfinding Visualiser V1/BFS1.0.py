from classes import Grid, Node

grid = Grid(["#?##?#", "#????#", "#??#?#", "#????#"])
noded_grid = grid.append_nodes()

def identify_node(grid_with_nodes, node_position):
    for row in grid_with_nodes:
        for node in row:
            if node.position == node_position:
                identified_node = node
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

            start_node = identify_node(grid_with_nodes, start_position)
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
        current_node = identify_node(grid_with_nodes, current)
        current_node.visit()
        grid.visualise_grid()
        print()

        if current == end_position:
            print(visited)
            print(visit_order)
            break

        for neighbour in current_node.get_neighbours():
            neighbour = identify_node(grid_with_nodes, neighbour)
            if neighbour is None:
                continue

            if neighbour.type != "wall":
                if neighbour.position not in visited:
                    neighbour.parent = current_node
                    neighbour.visit()
                    visited.add(neighbour.position)
                    visit_order.append(neighbour.position)
                    queue.append(neighbour.position)

    shortest_path = [start_position]
    shortest_path_visited = {start_position}
    
    for node_position in visit_order:
        if node_position not in shortest_path_visited:
            node = identify_node(grid_with_nodes, node_position)
            if node.parent.position in shortest_path_visited:
                if node.parent.child == None:
                    node.parent.child = node
                    shortest_path.append(node.position)
                    shortest_path_visited.add(node.position)
                
                else:
                    continue
                
            else:
                continue

        else:
            continue
    
    print(shortest_path)


bfs(noded_grid)
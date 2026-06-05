from classes import Grid

grid = Grid(["####", "#?##", "#??#", "####"])
noded_grid = grid.append_nodes()

def bfs(grid_with_nodes, start_position):
    queue = []
    for row in grid_with_nodes.layout:
        for column in row:
            if column.postion == start_position:
                queue.append(column)
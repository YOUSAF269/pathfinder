import time
from collections import deque
def get_neighbors(grid, cell):
    r, c = cell
    rows = len(grid)
    cols = len(grid[0])
    result = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
            result.append((nr, nc))
    return result
def build_path(came_from, goal):
    path = []
    cell = goal
    while cell is not None:
        path.append(cell)
        cell = came_from[cell]
    path.reverse()
    return path
def make_result(order, path, start_time):
    elapsed = (time.perf_counter() - start_time) * 1000
    return {"order": order, "path": path, "time_ms": elapsed}
def bfs(grid, start, goal):
    start_time = time.perf_counter()
    queue = deque([start])
    visited = {start}
    came_from = {start: None}
    order = []
    while queue:
        cell = queue.popleft()
        order.append(cell)
        if cell == goal:
            path = build_path(came_from, goal)
            return make_result(order, path, start_time)   
        for neighbor in get_neighbors(grid, cell):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = cell
                queue.append(neighbor)
    return make_result(order, [], start_time)             
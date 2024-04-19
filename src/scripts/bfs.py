from collections import deque


def bfs(graph, start, end):
    queue = deque([(start, [start], 0)])
    visited = set()
    paths = []
    costs = []

    while queue:
        node, path, cost = queue.popleft()

        visited.add(node)

        if node == end:
            paths.append(path)
            costs.append(cost)
            continue

        for neighbor, neighbor_cost in graph[node]:
            if neighbor not in visited and neighbor_cost > 0:
                new_path = path + [neighbor]
                new_cost = cost + neighbor_cost
                queue.append((neighbor, new_path, new_cost))

    if not paths:
        # Print if no path is found
        print("No path found from", start, "to", end)

    return paths, costs

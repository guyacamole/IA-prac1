def dfs(graph, start, end):  # aaaaaaaaaaa
    paths = []
    costs = []

    def dfs_recursive(node, path, cost, padre):
        if node == end:
            paths.append(path)
            costs.append(cost)
            return

        for neighbor, neighbor_cost in graph[node]:
            if padre != neighbor and neighbor not in path and neighbor_cost > 0:
                new_path = path + [neighbor]
                new_cost = cost + neighbor_cost
                dfs_recursive(neighbor, new_path, new_cost, node)

    dfs_recursive(start, [start], 0, start)

    if not paths:
        print("No path found from", start, "to", end)

    min_cost_index = costs.index(min(costs))
    return paths[min_cost_index], costs[min_cost_index]

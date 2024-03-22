from collections import defaultdict
from queue import PriorityQueue


def bfs_tree(graph, start):
    visited = set()
    queue = [start]
    bfs_tree = defaultdict(list)

    while queue:
        node = queue.pop(0)
        visited.add(node)
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                bfs_tree[node].append((neighbor, cost))

    return bfs_tree


def dfs_tree(graph, start):
    visited = set()
    stack = [start]
    dfs_tree = defaultdict(list)

    while stack:
        node = stack.pop()
        visited.add(node)
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                dfs_tree[node].append((neighbor, cost))

    return dfs_tree


def a_star_tree(graph, start, goal, heuristic):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))
    a_star_tree = defaultdict(list)

    while not queue.empty():
        _, node = queue.get()
        visited.add(node)

        if node == goal:
            break

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                priority = cost + heuristic(neighbor, goal)
                queue.put((priority, neighbor))
                a_star_tree[node].append((neighbor, cost))

    return a_star_tree


def print_tree(tree):
    level = 0
    for node, edges in tree.items():
        parent = get_parent(tree, node)  # Obtener el nodo padre
        # Imprimir nodo y su padre
        print("\t" * level + f"{node} (Padre: {parent}):")
        level += 1
        for edge in edges:
            print("\t" * level + f"├── {edge}")
        if not edges:
            print("\t" * level + "└──")


def get_parent(tree, node):
    for parent, edges in tree.items():
        for edge in edges:
            if edge[0] == node:
                return parent
    return None

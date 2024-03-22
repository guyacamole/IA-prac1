import numpy as np
from .terrain import get_terrain_type
from utils.constants import AGENTS_MOVEMENTS_COST
from .map import display_map
from .terrain import mark_positions
import time
import heapq
from collections import defaultdict


def load_agent(filename):
    with open(filename, 'r') as file:
        # read the first line into a variable
        agent_type = file.readline().strip()
        # read the remaining lines into a NumPy array
        agents_movement = np.array(file.readline().strip().split(','))

    return agent_type, agents_movement


def movement_controled(agente, map_data, movimientos, initial, objective):
    auxX, auxY = initial
    posX, posY = initial
    movement_cost = 0
    for movimiento in movimientos:
        print(movimiento)
        if movimiento == "left":
            auxX -= 1
        elif movimiento == "right":
            auxX += 1
        elif movimiento == "up":
            auxY += 1
        elif movimiento == "down":
            auxY -= 1
        else:
            raise ValueError("Invalid movement character")
        terrain_type, _, _ = get_terrain_type(map_data, auxX, auxY)
        # Get the movement cost for the current terrain agent_type
        movement_cost += AGENTS_MOVEMENTS_COST[(agente, terrain_type)]
        # Mark the current position as visited
        map_data = mark_positions(
            map_data, [((auxX, auxY), 'current'), ((posX, posY), 'visited')])
        # Display the map
        display_map(map_data)
        posY = auxY
        posX = auxX
        # Wait for 0.5 seconds
        time.sleep(0.5)
        if (auxX, auxY) == objective:
            print("Objective found!")
            print("Total movement cost: {}".format(movement_cost))
            break
    return


def create_graph(agent_type, map_data):
    graph = defaultdict(list)
    rows, cols, _ = map_data.shape

    for row in range(rows):
        for col in range(cols):
            cell = map_data[row, col]
            terrain, _, _ = cell

            # check neighboring cells
            for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n_row, n_col = row + d_row, col + d_col
                if 0 <= n_row < rows and 0 <= n_col < cols:

                    # calculate cost to move from cell to neighbor
                    cost = AGENTS_MOVEMENTS_COST[(agent_type, terrain)]
                    if cost == 0:
                        continue
                    # add edge to graph
                    graph[(row, col)].append(((n_row, n_col), cost))
    return graph


def astar(graph, start, end, heuristic):
    # Priority queue with tuples: (total_cost, current_node, path)
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        total_cost, node, path = heapq.heappop(queue)

        if node == end:
            return path, total_cost  # Return the path and its total cost

        if node in visited:
            continue

        visited.add(node)
        for neighbor, neighbor_cost in graph[node]:
            if neighbor not in visited and neighbor_cost > 0:
                new_path = path + [neighbor]
                priority = total_cost + neighbor_cost + \
                    heuristic(neighbor, end)
                heapq.heappush(queue, (priority, neighbor, new_path))

    print("No path found from", start, "to", end)  # Print if no path is found
    return [], float('inf')


def manhattan_distance(current, goal):

    x1, y1 = current
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)


def decide(paths, costs):
    return paths[costs.index(min(costs))], min(costs)


def move_agent(map_data, path, objective, cost):
    prev_move = None
    for i in range(len(path)):
        current_move = path[i]
        if i == 0:
            prev_move = current_move
        else:
            prev_move = path[i-1]
        map_data = mark_positions(
            map_data, [((current_move), 'current'), ((prev_move), 'visited')])
        display_map(map_data)  # display the map
        time.sleep(0.5)  # wait for 0.5 seconds
    if objective == current_move:
        print("Objective found!")
        print("Total movement cost: {}".format(cost))
    else:
        print("Objective not found!")

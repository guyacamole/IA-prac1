from scripts.map import load_map, display_map, scan_map
from scripts.agents import load_agent, movement_controled, create_graph, decide, move_agent
from scripts.agents import astar, manhattan_distance
from scripts.bfs import bfs
from scripts.tree import print_tree, bfs_tree, a_star_tree
from scripts.dfs import dfs


def main():
    map_data = load_map("data/map.txt")
    display_map(map_data)
    map_data, initial, objective = scan_map(map_data)
    while True:
        print("1. Solve by BFS")
        print("2. Solve by DFS")
        print("3. Solve by A*")
        print("4. Solve Manually")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if (choice == "1" or choice == "2" or choice == "3"):
            agent_type = input("Enter the agent type: ")
            graph = create_graph(agent_type, map_data)
        if choice == "1":
            paths, costs = bfs(graph, initial, objective)
            path, cost = decide(paths, costs)
            move_agent(map_data, path, objective, cost)
            tree = bfs_tree(graph, initial)
            print_tree(tree)
        elif choice == "2":
            # visited = set()
            paths, costs = dfs(graph, initial, objective)
            print(paths, costs)
            # path,cost = decide(paths,costs)
            # move_agent(map_data,path,objective,cost)
            # tree= dfs_tree(graph, initial)
            # print_tree(tree)
        elif choice == "3":
            path, cost = astar(graph, initial, objective, manhattan_distance)
            # move_agent(map_data,path,objective,cost)
            tree = a_star_tree(graph, initial, objective, manhattan_distance)
            print_tree(tree)
            # path,cost = decide(paths,costs)
            move_agent(map_data, path, objective, cost)
        elif choice == "4":
            agent_type, agent_movements = load_agent('agent.txt')
            movement_controled(agent_type, map_data,
                               agent_movements, initial, objective)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

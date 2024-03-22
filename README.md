# Practice Project

This practice project includes both Depth-First Search (DFS) and Breadth-First Search (BFS). The program receives a text file named `map.txt`. If you wish to move the agent manually, you should include another text file named `agent.txt`.

## Agent File

In the `agent.txt` file:

- The first line should contain the type of agent.
- The second line should contain the movements, as shown in the attached example.

## Map File

The map should have the following format for each cell `x:y:z`:

- `x` indicates the type of terrain. It should be an integer from 0 to 6 and will indicate if the cell has a mark.
- The map should only have two marked cells:
  - One with a 2, indicating the start.
  - One with a 5, indicating the goal.
- `z` indicates the visibility of the cell. It should be 1 for visible and 0 for invisible.

## Random Map Generation

A function is included that generates a random map. If you wish to test this, you can call it instead of the `load_map` function like so: `map_data = generar_mapa(<integer size of the map>)`.

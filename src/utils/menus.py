from .printer import map_menu, solver_options
from models.map import Map
from models.agent import Agent
from utils.constants import MOVEMENTS_COST


def menuMap(map: Map):
  menu_option = False
  while not menu_option:
    map_menu()
    option = input("Enter your choice: ")
    if option == "1":
      map.load_map()
      menu_option = True
    elif option == "2":
      map.generate_random_map(20, 20)
      menu_option = True
    else:
      print("Invalid choice. Please try again.")


def menuSolver(agent: Agent):
  solver_options()
  option = input("Enter your choice: ")
  if option == 1:
    agent.bfs()
  if option == 2:
    agent.dfs()
  if option == 3:
    agent.a()
  if option == 4:
    pass
  if option == 5:
    agent.emanuel()

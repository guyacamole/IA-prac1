import numpy as np


def load_agent(filename):
    with open(filename, 'r') as file:
        # read the first line into a variable
        agent_type = file.readline().strip()
        # read the remaining lines into a NumPy array
        agents_movement = np.array(file.readline().strip().split(','))

    return agent_type, agents_movement

import numpy as np
from utils.constants import TERRAIN_COLORS


def changeterrain_type(map_data, row, col, new_type):

    if not isinstance(map_data, np.ndarray):
        raise TypeError("map_data should be a numpy array")

    if row < 0 or row >= map_data.shape[0] or col < 0 or col >= map_data.shape[1]:
        raise ValueError("Invalid row or column index")

    if new_type not in TERRAIN_COLORS:
        raise ValueError("Invalid terrain agent_type")

    terrain_type, mark_value, visible = map_data[row, col]
    terrain_type = new_type
    map_data[row, col] = (terrain_type, mark_value, visible)

    return map_data


def get_terrain_type(map_data, row, col):
    if not isinstance(map_data, np.ndarray):
        raise TypeError("map_data should be a numpy array")

    if row < 0 or row >= map_data.shape[0] or col < 0 or col >= map_data.shape[1]:
        raise ValueError("Invalid row or column index")

    return map_data[row, col]


def mark_positions(map_data, positions):
    tag_dict = {
        'unnmarked': 0,
        'visited': 1,
        'initial': 2,
        'decision': 3,
        'current': 4,
        'objective': 5
    }

    for pos, tag in positions:
        # Get the tag character based on the tag name
        tag_char = tag_dict.get(tag, '')

        # If a valid tag character was found, mark the position
        if tag_char:
            terrain_type, mark_value, visible = map_data[pos[0], pos[1]]
            mark_value = tag_char
            map_data[pos[0], pos[1]] = (terrain_type, mark_value, visible)

    return map_data

TERRAIN_COLORS = {
    0: (0.5, 0.5, 0.5),  # Mountain - gray
    1: (0.9, 0.8, 0.5),  # Land - tan
    2: (0, 0, 1),  # Water - blue
    3: (1, 1, 0.5),  # Sand - light yellow
    4: (0, 0.6, 0),  # Forest - green
    5: (0.5, 0.5, 0.5),  # Swamp - purple
    6: (0, 0, 0)  # snow - white
}

MARK_SYMBOLS = {
    0: ' ',  # empty
    1: 'V',  # visited
    2: 'I',  # initial
    3: 'O',  # decision
    4: 'X',  # current
    5: 'XX'  # goal
}

MOVEMENTS_COST = {
    1: {
        'name': 'human',
        0: 0,  # Mountain
        1: 1,  # Land
        2: 2,  # Water
        3: 3,  # Sand
        4: 4,  # Forest
        5: 5,  # Swamp
        6: 5  # Snow
    },
    2: {
        'name': 'monkey',
        0: 0,  # Mountain
        1: 2,  # Land
        2: 4,  # Water
        3: 3,  # Sand
        4: 1,  # Forest
        5: 0,  # Swamp
        6: 0  # Snow
    },
    3: {
        'name': 'octopus',
        0: 0,  # Mountain
        1: 2,  # Land
        2: 1,  # Water
        3: 0,  # Sand
        4: 3,  # Forest
        5: 2,  # Swamp
        6: 0  # Snow
    },
    4: {
        'name': 'sasquatch',
        0: 15,  # Mountain
        1: 4,  # Land
        2: 0,  # Water
        3: 0,  # Sand
        4: 4,  # Forest
        5: 0,  # Swamp
        6: 0  # Snow
    }
}

AGENTS_MOVEMENTS_COST = {
    ('human', 0): 0,  # Human agent cost to traverse mountain terrain
    ('human', 1): 1,  # Human agent cost to traverse land terrain
    ('human', 2): 2,  # Human agent cost to traverse water terrain
    ('human', 3): 3,  # Human agent cost to traverse sand terrain
    ('human', 4): 4,  # Human agent cost to traverse forest terrain
    ('human', 5): 5,  # Human agent cost to traverse swamp terrain
    ('human', 6): 5,  # Human agent cost to traverse snow terrain

    ('monkey', 0): 0,  # Monkey agent cost to traverse mountain terrain
    ('monkey', 1): 2,  # Monkey agent cost to traverse land terrain
    ('monkey', 2): 4,  # Monkey agent cost to traverse water terrain
    ('monkey', 3): 3,  # Monkey agent cost to traverse sand terrain
    ('monkey', 4): 1,  # Monkey agent cost to traverse forest terrain
    ('monkey', 5): 0,  # Monkey agent cost to traverse swamp terrain
    ('monkey', 6): 0,  # Monkey agent cost to traverse snow terrain

    ('octopus', 0): 0,  # Octopus agent cost to traverse mountain terrain
    ('octopus', 1): 2,  # Octopus agent cost to traverse land terrain
    ('octopus', 2): 1,  # Octopus agent cost to traverse water terrain
    ('octopus', 3): 0,  # Octopus agent cost to traverse sand terrain
    ('octopus', 4): 3,  # Octopus agent cost to traverse forest terrain
    ('octopus', 5): 2,  # Octopus agent cost to traverse swamp terrain
    ('octopus', 6): 0,  # Octopus agent cost to traverse snow terrain

    ('sasquatch', 0): 15,  # sasquatch agent cost to traverse mountain terrain
    ('sasquatch', 1): 4,  # sasquatch agent cost to traverse land terrain
    ('sasquatch', 2): 0,  # sasquatch agent cost to traverse water terrain
    ('sasquatch', 3): 0,  # sasquatch agent cost to traverse sand terrain
    ('sasquatch', 4): 4,  # sasquatch agent cost to traverse forest terrain
    ('sasquatch', 5): 0,  # sasquatch agent cost to traverse swamp terrain
    ('sasquatch', 6): 0,  # sasquatch agent cost to traverse snow terrain
}

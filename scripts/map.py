from matplotlib import patches, collections as coll
import random
import numpy as np
from utils.constants import TERRAIN_COLORS, MARK_SYMBOLS
import matplotlib.pyplot as plt


def generar_mapa(n):
    # Crear una matriz vacía de tamaño n x n
    mapa = [[None] * n for _ in range(n)]

    # Llenar la matriz con valores aleatorios que cumplan las características
    for i in range(n):
        for j in range(n):
            # El valor y es 0, excepto en dos celdas que deben tener 2 y 5
            if (i == 0 and j == 1) or (i == n-1 and j == n-2):
                y = random.choice([2, 5])
            else:
                y = 0

            # El valor x es un entero entre 0 y 6, donde 0 representa una barrera
            x = random.randint(0, 6)

            # El valor z es 0 o 1
            z = random.randint(0, 1)

            # Guardar los valores en la celda correspondiente
            mapa[i][j] = (x, y, z)

    # Convertir la matriz a un array de numpy
    mapa_array = np.array(mapa)

    return mapa_array


def load_map(filename):
    with open(filename, 'r') as f:
        map_string = f.read()
    map_data = [[tuple(map(int, cell.split(':'))) for cell in row.split(',')]
                for row in map_string.split('\n') if row]
    return np.array(map_data)


def display_map(map_array, map_name='map.png'):
    # create a colormap from the terrain colors
    # colors.ListedColormap([TERRAIN_COLORS[i]
    #                        for i in TERRAIN_COLORS.keys()])

    # create a new figure and axis for the map plot
    fig, ax = plt.subplots(figsize=(10, 10))

    # create a new array for the map with the same shape as the input array, but with dtype=object
    display_array = np.empty(map_array.shape, dtype=object)

    # iterate over the input array and create a colored patch for each terrain agent_type
    for i in range(map_array.shape[0]):
        for j in range(map_array.shape[1]):
            terrain_type, mark_value, visible = map_array[i, j]

            if visible == 0:
                # if the cell is not visible, color it black
                display_array[i, j] = patches.Rectangle(
                    (j, i), 1, 1, linewidth=1, edgecolor='black', facecolor='black')
            else:
                # otherwise, color it according to the terrain agent_type
                display_array[i, j] = patches.Rectangle(
                    (j, i), 1, 1, linewidth=1, edgecolor='black', facecolor=TERRAIN_COLORS[terrain_type])

                if mark_value != 0:
                    # add a mark symbol if there is a mark value
                    mark_symbol = MARK_SYMBOLS[mark_value]
                    ax.text(j + 0.5, i + 0.5, mark_symbol, fontsize=12,
                            ha='center', va='center', color='black')

    # create a PatchCollection from the patch objects and add it to the plot axis
    pc = coll.PatchCollection(display_array.reshape(-1), match_original=True)
    ax.add_collection(pc)

    # set axis limits and labels
    ax.set_xlim(0, map_array.shape[1])
    ax.set_ylim(map_array.shape[0], 0)

    ax.set_xlabel('Column')
    ax.set_ylabel('Row')
    ax.set_title('Map')
    plt.savefig(map_name)
    # plt.show()  # This line was added


def scan_map(map_data):
    for row in range(map_data.shape[0]):
        for col in range(map_data.shape[1]):
            terrain_type, mark_value, visible = map_data[row, col]
            visible = 1
            if mark_value == 2:
                initial = (row, col)
            elif mark_value == 5:
                objective = (row, col)
            map_data[row, col] = (terrain_type, mark_value, visible)

    return map_data, initial, objective

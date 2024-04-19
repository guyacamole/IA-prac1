import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches, collections as coll
from utils.constants import TERRAIN_COLORS, MARK_SYMBOLS
import logging
from pathlib import Path


class Map:
  """A class to represent a map."""

  def __init__(self):
    """Initialize an empty map."""
    self._map = None
    self._mapBackup = None
    self.__initial__ = None
    self.__objective__ = None

  @property
  def map(self):
    return self._map

  @map.setter
  def map(self, map_array):
    if isinstance(map_array, np.ndarray):
      self._map = map_array
    else:
      raise ValueError("map must be a numpy array")

  @property
  def mapBackup(self):
    return self._mapBackup

  @mapBackup.setter
  def mapBackup(self, map_array):
    if isinstance(map_array, np.ndarray):
      self._mapBackup = map_array
    else:
      raise ValueError("mapBackup must be a numpy array")

  def reset_map(self):
    """Reset the map to its initial state."""
    if self.mapBackup is not None:
      self.map = self.mapBackup

  def load_map(self, filename='./src/data/map.txt'):
    """Load a map from a file or create an empty one if no file is provided."""
    if filename is None:
      return

    filepath = Path(filename)
    if not filepath.exists():
      logging.error(f"File {filename} not found.")
      return

    try:
      with filepath.open('r') as f:
        map_string = f.read()
      map_data = [[tuple(map(int, cell.split(':'))) for cell in row.split(',')]
                  for row in map_string.split('\n') if row]
      self.map = self.mapBackup = np.array(map_data)
    except ValueError:
      logging.error(f"File {filename} is not in the expected format.")

  def generate_random_map(self, width, height):
    """Generate a random map of the given size."""
    random_map = np.zeros((width, height, 3), dtype=int)
    random_map[..., 0] = np.random.randint(0, 7, (width, height))  # x values
    random_map[..., 2] = np.random.randint(0, 2, (width, height))  # z values
    random_map[0, 1, 1] = random_map[-1, -2,
                                     1] = np.random.choice([2, 5])  # y values
    self.map = self.mapBackup = random_map

  def display_map(self, map_name='map.png'):
    """Print the map to the console."""
    if self.map is None:
      logging.error("Map has not been initialized.")
      return

    fig, ax = plt.subplots(figsize=(10, 10))
    display_array = np.empty(self.map.shape, dtype=object)

    for i in range(self.map.shape[0]):
      for j in range(self.map.shape[1]):
        terrain_type, mark_value, visible = self.map[i, j]

        if visible == 0:
          display_array[i, j] = patches.Rectangle(
              (j, i), 1, 1, linewidth=1, edgecolor='black', facecolor='black')
        else:
          display_array[i, j] = patches.Rectangle(
              (j, i), 1, 1, linewidth=1, edgecolor='black', facecolor=TERRAIN_COLORS[terrain_type])

          if mark_value != 0:
            mark_symbol = MARK_SYMBOLS[mark_value]
            ax.text(j + 0.5, i + 0.5, mark_symbol, fontsize=12,
                    ha='center', va='center', color='black')

    pc = coll.PatchCollection(display_array.reshape(-1), match_original=True)
    ax.add_collection(pc)

    ax.set_xlim(0, self.map.shape[1])
    ax.set_ylim(self.map.shape[0], 0)

    ax.set_xlabel('Column')
    ax.set_ylabel('Row')
    ax.set_title('Map')
    plt.savefig(map_name)

from scripts.map import load_map, display_map


def main():
    map_data = load_map("data/map.txt")
    display_map(map_data)


if __name__ == "__main__":
    main()

from collections import deque
from pprint import pprint


class Node:
    def __init__(self, x, y, parent=None):
        self._x = x
        self._y = y
        self._parent = parent

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return str((self.x, self.y))


ROWS = 0
COLUMNS = 0

SOURCE: list
DESTINATION: list
SOURCE_VALUE = "S"
DESTINATION_VALUE = "E"
HIGHEST_ELEVATION = "z"
SHORTEST_ELEVATION = "a"

DIRECTION = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}
WAY = {
    "R": ">",
    "L": "<",
    "U": "^",
    "D": "V",
}


def read_map(path):
    global ROWS, COLUMNS, SOURCE, DESTINATION

    file = open(path)

    height_map = []
    i = 0
    for line in file.readlines():
        line = line.replace("\n", "")

        height_map.append([])
        j = 0
        for value in line:
            height_map[i].append(value)

            if value == SOURCE_VALUE:
                SOURCE = [i, j]
            elif value == DESTINATION_VALUE:
                DESTINATION = [i, j]

            j += 1

        i += 1

    ROWS = len(height_map)
    COLUMNS = len(height_map[0])

    return height_map


def check_coords(x, y):
    # if we are outside the map
    if not (0 <= x < ROWS and 0 <= y < COLUMNS):
        return False
    return True


def check_validity(current_value, parent_value):
    # if the difference between the ascii code is bigger than 1 or if we reach the destination but not from
    # the highest point => return false
    if (ord(current_value) - ord(parent_value) > 1 and\
            parent_value != SOURCE_VALUE) or \
            (parent_value != HIGHEST_ELEVATION and current_value == DESTINATION_VALUE):
        return False
    return True


def get_path(node, path, height_map):
    if not node:
        return path
    else:
        path.appendleft(node)

        # # replace the values in the map with the direction
        # for direction in DIRECTION.keys():
        #     # verify the parent if not None for the last Node put in the path list
        #     if node.parent is not None and \
        #             node.parent.x + DIRECTION[direction][0] == node.x and \
        #             node.parent.y + DIRECTION[direction][1] == node.y:
        #         height_map[node.parent.x][node.parent.y] = WAY[direction]

        return get_path(node.parent, path, height_map)


def find_path(height_map):
    """
    Breath first search for the shortest path.
    :param height_map: matrix of characters
    :return: list of tuples of twi integers => the path
    """
    queue = deque()
    source = Node(SOURCE[0], SOURCE[1])
    queue.append(source)

    visited = set()
    visited.add(tuple(SOURCE))

    while queue:

        current = queue.popleft()
        value = height_map[current.x][current.y]

        if value == DESTINATION_VALUE:
            return get_path(current, deque(), height_map)

        for direction_coords in DIRECTION.keys():
            x = current.x + DIRECTION[direction_coords][0]
            y = current.y + DIRECTION[direction_coords][1]

            if check_coords(x, y) and check_validity(height_map[x][y], value):
                next = Node(x, y, current)

                if (x, y) not in visited:
                    queue.append(next)
                    visited.add((x, y))


def find_path_2(height_map, start):
    """
    Breath first search for the shortest path.
    :param height_map: matrix of characters
    :return: list of tuples of twi integers => the path
    """
    queue = deque()
    source = Node(start[0], start[1])
    queue.append(source)

    visited = set()
    visited.add(tuple(start))

    while queue:

        current = queue.popleft()
        value = height_map[current.x][current.y]

        if value == DESTINATION_VALUE:
            return len(get_path(current, deque(), height_map))

        for direction_coords in DIRECTION.keys():
            x = current.x + DIRECTION[direction_coords][0]
            y = current.y + DIRECTION[direction_coords][1]

            if check_coords(x, y) and check_validity(height_map[x][y], value):
                next = Node(x, y, current)

                if (x, y) not in visited:
                    queue.append(next)
                    visited.add((x, y))


def algorithm(height_map):

    paths_lengths = []
    for i in range(0, len(height_map)):
        for j in range(0, len(height_map[i])):

            if height_map[i][j] == SHORTEST_ELEVATION:
                steps = find_path_2(height_map, (i, j))
                # for the case we have no path to destination
                if steps is not None:
                    paths_lengths.append(steps - 1)

    smallest = min(paths_lengths)
    return smallest


def main():
    height_map = read_map("input.txt")
    print(algorithm(height_map))
    # path = find_path(height_map)
    # for row in height_map:
    #     for value in row:
    #         print(value, end="")
    #     print()
    # print(len(path) - 1)


if __name__ == '__main__':
    main()

from copy import deepcopy

MAXIM = 500
HEAD_COORDS = [MAXIM/2, MAXIM/2]
TAIL_COORDS = [MAXIM/2, MAXIM/2]
START = [MAXIM/2, MAXIM/2]

DIRECTION = {
    "0": (0, 0),
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
    "RU": (-1, 1),
    "LU": (-1, -1),
    "RD": (1, 1),
    "LD": (1, -1)
}
SNAKE_TAIL = []
for i in range(1, 10):
    SNAKE_TAIL.append([START[0], START[1]])


def head_in_position(row, column):
    return HEAD_COORDS == [row, column]


def tail_near_head():

    is_near = False
    for dir in DIRECTION.keys():
        is_near = is_near or head_in_position(TAIL_COORDS[0] + DIRECTION[dir][0],
                                              TAIL_COORDS[1] + DIRECTION[dir][1])

        if is_near:
            return True

    return False


def near_front_neighbour(next, current):

    for dir in DIRECTION.keys():

        if [current[0] + DIRECTION[dir][0], current[1] + DIRECTION[dir][1]] == [next[0], next[1]]:
            return True

    return False


def read_moves(path):
    file = open(path)

    moves = []

    for line in file.readlines():
        moves.append(line.replace("\n", "").split(" "))

    return moves


def algorithm(bridge, moves):

    global HEAD_COORDS
    for move in moves:
        direction = move[0]
        times = int(move[1])

        for i in range(0, times):
            HEAD_COORDS = [HEAD_COORDS[0] + DIRECTION[direction][0],
                           HEAD_COORDS[1] + DIRECTION[direction][1]]

            if not tail_near_head():
                new_row = (TAIL_COORDS[0] + HEAD_COORDS[0]) / 2
                new_column = (TAIL_COORDS[1] + HEAD_COORDS[1]) / 2

                if int(new_row) != new_row:     # if it is .5
                    TAIL_COORDS[0] = HEAD_COORDS[0]
                else:
                    TAIL_COORDS[0] = new_row

                if int(new_column) != new_column:
                    TAIL_COORDS[1] = HEAD_COORDS[1]
                else:
                    TAIL_COORDS[1] = new_column

                bridge[int(TAIL_COORDS[0])][int(TAIL_COORDS[1])] = "#"

    bridge[int(START[0])][int(START[1])] = "#"

    total = 0
    for row in bridge:
        for value in row:

            if value == "#":
                total += 1
            # print(value, end=" ")
        # print()
    print(total)

# this is better for snake games:)))) ------------------------------------------------------------------
# def algorithm_2(bridge, moves):
#
#     global HEAD_COORDS
#     for move in moves:
#         direction = move[0]
#         times = int(move[1])
#
#            # keep the coords of first unchanged
#         for i in range(0, times):
#             # prev = deepcopy(SNAKE_TAIL[0])
#             HEAD_COORDS = [HEAD_COORDS[0] + DIRECTION[direction][0],
#                            HEAD_COORDS[1] + DIRECTION[direction][1]]
#
#             if not near_front_neighbour(HEAD_COORDS, SNAKE_TAIL[0]):  # first point in snake's body
#                 new_row = (SNAKE_TAIL[0][0] + HEAD_COORDS[0]) / 2
#                 new_column = (SNAKE_TAIL[0][1] + HEAD_COORDS[1]) / 2
#
#                 if int(new_row) != new_row:     # if it is .5
#                     SNAKE_TAIL[0][0] = HEAD_COORDS[0]
#                 else:
#                     SNAKE_TAIL[0][0] = new_row
#
#                 if int(new_column) != new_column:
#                     SNAKE_TAIL[0][1] = HEAD_COORDS[1]
#                 else:
#                     SNAKE_TAIL[0][1] = new_column
#
#             front = deepcopy(SNAKE_TAIL[0])
#
#             for i in range(1,9):
#
#                 if not near_front_neighbour(front, SNAKE_TAIL[i]):
#                     front = deepcopy(SNAKE_TAIL[i])     # used as auxiliary var
#                     SNAKE_TAIL[i] = deepcopy(prev)
#                     prev = deepcopy(front)
#                     front = deepcopy(SNAKE_TAIL[i])
#                 else:
#                     break
#
#                 if i == len(SNAKE_TAIL) - 1:
#                     bridge[int(SNAKE_TAIL[-1][0])][int(SNAKE_TAIL[-1][1])] = "#"
# ----------------------------------------------------------------------------------------------------


def algorithm_2(bridge, moves):

    global HEAD_COORDS
    for move in moves:
        direction = move[0]
        times = int(move[1])

        for i in range(0, times):
            HEAD_COORDS = [HEAD_COORDS[0] + DIRECTION[direction][0],
                           HEAD_COORDS[1] + DIRECTION[direction][1]]

            front = deepcopy(HEAD_COORDS)
            for i in range(0, 9):

                # move each part od the rope after the point in front
                if not near_front_neighbour(front, SNAKE_TAIL[i]):
                    new_row = (SNAKE_TAIL[i][0] + front[0]) / 2
                    new_column = (SNAKE_TAIL[i][1] + front[1]) / 2

                    if int(new_row) != new_row:  # if it is .5
                        SNAKE_TAIL[i][0] = front[0]
                    else:
                        SNAKE_TAIL[i][0] = new_row

                    if int(new_column) != new_column:
                        SNAKE_TAIL[i][1] = front[1]
                    else:
                        SNAKE_TAIL[i][1] = new_column
                else:
                    break

                if i == len(SNAKE_TAIL) - 1:
                    bridge[int(SNAKE_TAIL[-1][0])][int(SNAKE_TAIL[-1][1])] = "#"

                front = SNAKE_TAIL[i]

    bridge[int(START[0])][int(START[1])] = "#"

    total = 0
    for row in bridge:
        for value in row:

            if value == "#":
                total += 1
            # print(value, end=" ")
        # print()
    print(total)


def main():
    bridge = [["." for i in range(0, MAXIM)] for j in range(0, MAXIM)]
    moves = read_moves("input.txt")
    # algorithm(bridge, moves)
    algorithm_2(bridge, moves)


if __name__ == '__main__':
    main()

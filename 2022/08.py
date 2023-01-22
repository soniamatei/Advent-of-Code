from enum import Enum


class Movements(Enum):
    LEFT = [0, -1]
    UP = [-1, 0]
    RIGHT = [0, 1]
    DOWN = [1, 0]


def read_matrix(path):
    file = open(path)
    lines = file.readlines()

    matrix = [[int(line[i]) for i in range(0, len(line.replace("\n", "")))] for line in lines]
    return matrix


def move(matrix, direction, row, column, value):
    if row == 0 or row == len(matrix) - 1 or \
            column == 0 or column == len(matrix[0]) - 1:
        return True

    elif matrix[row + direction[0]][column + direction[1]] >= value:
        return False

    return move(matrix, direction, row + direction[0], column + direction[1], value)


def algorithm(matrix):
    total_trees_visible = 0

    i = 0
    for row in matrix:
        j = 0
        for value in row:

            if move(matrix, Movements.LEFT.value, i, j, value) or \
                    move(matrix, Movements.UP.value, i, j, value) or \
                    move(matrix, Movements.RIGHT.value, i, j, value) or \
                    move(matrix, Movements.DOWN.value, i, j, value):
                total_trees_visible += 1

            j += 1
        i += 1

    print(total_trees_visible)


def move_2(matrix, direction, row, column, value, score):
    if row + direction[0] < 0 or row + direction[0] >= len(matrix) or \
            column + direction[1] < 0 or column + direction[1] >= len(matrix[0]):
        return score

    if matrix[row + direction[0]][column + direction[1]] >= value:
        return score + 1

    return move_2(matrix, direction, row + direction[0], column + direction[1], value, score + 1)


def algorithm_2(matrix):

    scenic_scores_collection = []

    i = 0
    for row in matrix:
        j = 0
        for value in row:

            scenic_score = move_2(matrix, Movements.LEFT.value, i, j, value, 0) * \
                           move_2(matrix, Movements.UP.value, i, j, value, 0) * \
                           move_2(matrix, Movements.RIGHT.value, i, j, value, 0) * \
                           move_2(matrix, Movements.DOWN.value, i, j, value, 0)

            scenic_scores_collection.append(scenic_score)

            j += 1
        i += 1

    largest = max(scenic_scores_collection)
    print(largest)


def main():
    matrix = read_matrix("input.txt")
    # algorithm(matrix)
    algorithm_2(matrix)


if __name__ == '__main__':
    main()

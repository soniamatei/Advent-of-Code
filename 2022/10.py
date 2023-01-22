SPRITE = [0, 1, 2]
CRT = [["." for i in range(0, 40)] for j in range(0, 6)]


def read_program(path):
    file = open(path)

    program = []
    for line in file.readlines():
        program.append(line.replace("\n", "").split(" "))

    return program


def check_cycle(cycle):

    for imp_cycle in [20, 60, 100, 140, 180, 220]:
        if cycle == imp_cycle:
            return True

    return False


def algorithm(program):

    total_signal_strength = 0
    cycle = 1
    register_X = 1
    for cmd in program:

        if cmd[0] == "noop":
            cycle += 1
        else:
            cycle += 1
            if check_cycle(cycle):
                total_signal_strength += cycle * register_X
            cycle += 1
            register_X += int(cmd[1])

        if check_cycle(cycle):
            total_signal_strength += cycle * register_X

    return total_signal_strength


def algorithm_2(program):

    global SPRITE

    row = 0
    column = 0
    for cmd in program:

        if column % 40 == 0 and column != 0:    # go on new line if reach edge of crt
            row += 1
            column = 0

        if column in SPRITE:    # drawing pixel
            CRT[row][column] = "#"

        if cmd[0] == "noop":
            column += 1
        else:
            column += 1

            if column in SPRITE:    # drawing pixel
                CRT[row][column] = "#"

            column += 1
            SPRITE = [int(cmd[1]) + i for i in SPRITE]

    for i in range(0, 6):
        for j in range(0, 40):
            print(CRT[i][j], end=" ")
        print()


def main():
    program = read_program("input.txt")
    # print(algorithm(program))
    algorithm_2(program)


if __name__ == '__main__':
    main()

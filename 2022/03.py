import string

PRIORITY = list(string.ascii_letters)

def read_backpacks(path):
    file = open(path)

    backpacks = []

    for line in file.readlines():
        line = line.replace("\n", "")

        first_compartment, second_compartment = line[:len(line) // 2], line[len(line) // 2:]
        backpacks.append([[*first_compartment], [*second_compartment]])

    return backpacks


def read_backpacks_2(path):
    file = open(path)

    backpacks = []

    for line in file.readlines():
        backpacks.append([*line.replace("\n", "")])

    return backpacks


def algorithm(backpacks):

    total_priorities = 0
    for bp in backpacks:
        common_item = set(bp[0]) & set(bp[1])
        common_item = list(common_item)     # take values from set in list
        total_priorities += PRIORITY.index(common_item[0]) + 1      # plus 1 because the counting begins from 0 and a has value 1

    return total_priorities


def algorithm_2(backpacks):

    total_priorities = 0
    for i in range(0, len(backpacks), 3):

        common_item = set(backpacks[i]) & set(backpacks[i+1]) & set(backpacks[i+2])
        common_item = list(common_item)     # take values from set in list
        total_priorities += PRIORITY.index(common_item[0]) + 1      # plus 1 because the counting begins from 0 and a has value 1

    return total_priorities

def main():
    # backpacks = read_backpacks("input.txt")
    backpacks = read_backpacks_2("input.txt")
    # print(algorithm(backpacks))
    print(algorithm_2(backpacks))


if __name__ == '__main__':
    main()

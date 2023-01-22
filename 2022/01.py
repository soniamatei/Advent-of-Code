
def read_calorie_per_elf(path):
    file = open(path)
    lines = file.readlines()

    calories_per_elf = []
    calorie = 0

    for line in lines:
        line.replace("\n", "")

        if line == "\n":
            calories_per_elf.append(calorie)
            calorie = 0

        else:
            calorie += int(line)
    calories_per_elf.append(calorie)

    return calories_per_elf


def sum_top_three_calories(calories_per_elf):

    total = 0
    for i in range(0, 3):
        maxim = max(calories_per_elf)
        calories_per_elf.remove(maxim)
        total += maxim

    return total


def main():
    calories_per_elf = read_calorie_per_elf("input.txt")
    print(calories_per_elf)
    print(max(calories_per_elf))
    print(sum_top_three_calories(calories_per_elf))


if __name__ == '__main__':
    main()

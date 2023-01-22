from math import trunc
from pprint import pprint
import numpy as np

GIGA_CHAD = 0


def read_monkeys(path):
    file = open(path)

    monkeys = {}

    i = 0
    monkey = file.readline()
    while monkey:
        # initialize database for monkey
        monkeys[i] = {}

        # read items
        garbage = file.readline().replace("\n", "").strip().split(' ', 2)
        items = [int(x) for x in garbage[2].split(", ")]
        monkeys[i]["items"] = items

        # read operation
        garbage = file.readline().replace("\n", "").strip().split(" ", 3)
        operation = garbage[3].split(" ")
        monkeys[i]["operation"] = operation

        # read test
        garbage = file.readline().replace("\n", "").strip().split(" ")
        test = garbage[3]
        monkeys[i]["division by"] = int(test)

        # read if true
        garbage = file.readline().replace("\n", "").strip().split(" ")
        if_true = garbage[5]
        monkeys[i]["monkey for true"] = int(if_true)

        # read if false
        garbage = file.readline().replace("\n", "").strip().split(" ")
        if_false = garbage[5]
        monkeys[i]["monkey for false"] = int(if_false)

        i += 1
        file.readline()     # miss the empty line
        monkey = file.readline()

    return monkeys


def get_worry_level(first, operand, second, replacement):

    if first == "old":
        first = replacement
    else:
        first = int(first)

    if second == "old":
        second = replacement
    else:
        second = int(second)

    first = first
    second = second

    result = 0
    if operand == "+":
        result = (first + second) % GIGA_CHAD
    elif operand == "*":
        result = (first * second) % GIGA_CHAD
    return result


def calculate_least_common_multiple(monkeys):
    lcm = np.longlong(1)
    for id in monkeys.keys():
        lcm *= monkeys[id]["division by"]

    return lcm


def algorithm(monkeys):

    global GIGA_CHAD
    GIGA_CHAD = calculate_least_common_multiple(monkeys)

    inspections = []
    for monkey in monkeys.keys():
        inspections.append(0)

    for round in range(0, 10000):
        for monkey_id in monkeys.keys():
            for item in monkeys[monkey_id]["items"]:

                operation = monkeys[monkey_id]["operation"]
                worry_level = get_worry_level(operation[0], operation[1], operation[2], item)

                # worry_level_after_relief = trunc(worry_level / 3)

                # check to which monkey to pass the item to
                if worry_level % monkeys[monkey_id]["division by"] == 0:
                    throw_to_monkey_id = monkeys[monkey_id]["monkey for true"]
                else:
                    throw_to_monkey_id = monkeys[monkey_id]["monkey for false"]

                # pass the item with the current worry level
                monkeys[throw_to_monkey_id]["items"].append(worry_level)

                # increase the inspection to monkey
                inspections[monkey_id] += 1

            # empty their list for not having any items anymore
            monkeys[monkey_id]["items"].clear()

    print(inspections)
    inspections = sorted(inspections)
    return inspections[-1] * inspections[-2]


def main():
    monkeys = read_monkeys("input.txt")
    monkey_business = algorithm(monkeys)
    pprint(monkey_business)


if __name__ == '__main__':
    main()

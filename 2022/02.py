
opponent = {
    "A" : "Rock",
    "B" : "Paper",
    "C" : "Scissors"
}

me = {
    "X" : "Rock",
    "Y" : "Paper",
    "Z" : "Scissors"
}

me2 = {
    "A" : {
        "X" : "Scissors",
        "Y" : "Rock",
        "Z" : "Paper"
    },
    "B" : {
        "X" : "Rock",
        "Y" : "Paper",
        "Z" : "Scissors"
    },
    "C" : {
        "X" : "Paper",
        "Y" : "Scissors",
        "Z" : "Rock"
    }
}

round_outcome = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

combinations = { # from my perspective
    "Rock" : {
        "Rock" : 3,
        "Paper" : 0,
        "Scissors" : 6
    },
    "Paper" : {
        "Rock" : 6,
        "Paper" : 3,
        "Scissors" : 0
    },
    "Scissors" : {
        "Rock" : 0,
        "Paper" : 6,
        "Scissors" : 3
    }
}

values = {
    "Rock" : 1,
    "Paper" : 2,
    "Scissors" : 3
}


def read_strategy_guide(path):
    file = open(path)

    list_strategy_guide = []

    for line in file.readlines():
        list_strategy_guide.append(line.replace("\n", "").split(" "))

    return list_strategy_guide


def algorithm(list_strategy_guide):
    total_score = 0

    for round in list_strategy_guide:
        opponent_choice = opponent[round[0]]    # string with choice
        my_choice = me[round[1]]
        total_score += values[my_choice] + combinations[my_choice][opponent_choice]

    return total_score


def algorithm_2(list_strategy_guide):
    total_score = 0

    for round in list_strategy_guide:
        my_choice = me2[round[0]][round[1]]
        # print(total_score)
        total_score += values[my_choice] + round_outcome[round[1]]

    return total_score


def main():
    list_strategy_guide = read_strategy_guide("input.txt")
    # print(algorithm(list_strategy_guide))
    print(algorithm_2(list_strategy_guide))

if __name__ == '__main__':
    main()

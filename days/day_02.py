from get_day_input import get_input
import math

data = get_input(2).splitlines()
# print(data)

test_data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
             "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
             "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
             "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
             "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
             ]


def function_one(data_):
    max_red = 12
    max_green = 13
    max_blue = 14
    intermediate = 0
    score = 0
    for i, line in enumerate(data_):
        game = line.split(':')[1].split(';')
        print(game)
        for throw in game:
            print(throw.split(','))
            for elem in throw.split(','):
                print(elem.strip())
                match elem.strip().split():
                    case [r, "red"]:
                        if int(r) > max_red:
                            print("max red")
                            intermediate += 1
                    case [b, "blue"]:
                        if int(b) > max_blue:
                            print("max blue")
                            intermediate += 1
                    case [g, "green"]:
                        if int(g) > max_green:
                            print("max green")
                            intermediate += 1
        if intermediate == 0:
            score += (i + 1)
        intermediate = 0
    return score


print(function_one(data))


def function_two(data_):
    max_red = 0
    max_green = 0
    max_blue = 0
    score_card = []
    score = 0
    total_card = []
    total_score = 0
    for i, line in enumerate(data_):
        game = line.split(':')[1].split(';')
        for throw in game:
            for elem in throw.split(','):
                match elem.strip().split():
                    case [r, "red"]:
                        if int(r) > max_red:
                            max_red = int(r)
                    case [b, "blue"]:
                        if int(b) > max_blue:
                            max_blue = int(b)
                    case [g, "green"]:
                        if int(g) > max_green:
                            max_green = int(g)
        score_card.append(max_red)
        score_card.append(max_green)
        score_card.append(max_blue)
        score = math.prod(score_card)
        total_card.append(score)
        max_red = 0
        max_blue = 0
        max_green = 0
        score_card = []
    return sum(total_card)


answer2 = function_two(data)
print("Part 2: ", answer2)

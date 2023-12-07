from get_day_input import get_input

data = get_input(4).splitlines()

# print(data)
test1 = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
         "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
         "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
         "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
         "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
         "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]


def function_one(dat):
    total_winning_number = 0
    total_card = 0
    total = 0
    for i, line in enumerate(dat):
        l1 = dat[i].split(':')
        l2 = l1[1].split('|')
        string_win = l2[0]
        string_card = l2[1]
        list_win = list(string_win.split(" "))
        list_card = list(string_card.split(" "))
        while "" in list_win:
            list_win.remove("")
        while "" in list_card:
            list_card.remove("")
        # print(list_win)
        # print(list_card)
        for num in list_win:
            for elem in list_card:
                if num == elem:
                    total_winning_number += 1
        # print("total winning number ", total_winning_number)
        if total_winning_number > 0:
            total_card = pow(2, total_winning_number - 1)
        # print("total card ", total_card)
        total_winning_number = 0
        total += total_card
        total_card = 0
    return total


score = function_one(data)
print("Part 1: ", score)


def function_two(data2):
    """
    Create dict to keep count of number of copies.
    card_dict.update({i + 1 : 0}) -> added + 1 because we start with card 1
    """
    copies = {i: 1 for i in range(len(data2))}
    winning_numbers = 0
    for i, line in enumerate(data2):
        l1 = data2[i].split(':')
        l2 = l1[1].split('|')
        list_win = list(l2[0].strip().split())
        list_card = list(l2[1].strip().split())
        print(list_win)
        print(list_card)
        print(copies)
        for num in list_win:
            for elem in list_card:
                if num == elem:
                    winning_numbers += 1
        for j in range(winning_numbers):
            # check if key exists and then add copies[i] to take into account the copies
            if i+1+j in copies:
                copies[i+1+j] += copies[i]
        winning_numbers = 0
    return sum(copies.values())


score2 = function_two(data)
print("Part 2: ", score2)

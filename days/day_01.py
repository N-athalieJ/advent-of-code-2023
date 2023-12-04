from get_day_input import get_input

data = get_input(1).splitlines()
total_list = []


# Part 1
def get_int_from_line():
    """
    1. Loop through each character - of a string - in the data input.
    2. Check if the character is an integer. If so, add to the digits[].
    3. Create a pair of the first and last digit in the digits[].
    4. Append this pair to the total list and empty the digits[].
    """
    digits = []
    for elem in data:
        for i in elem:
            if i.isdigit():
                digits.append(i)
        int_pair = (digits[0] + digits[-1])
        total_list.append(int(int_pair))
        digits.clear()


get_int_from_line()
total = sum(total_list)
print("Answer Part 1: ", total)

# Part 2
dictionary = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open("output_dominique.txt", "r") as f:
    """
    r = read
    w = write
    with open -> opent en sluit de file automatisch. Dit is een clean manier anders als je hem opent dan 'sluit hij hem nooit.
    """
    answers = f.read().splitlines()


def get_elem_from_data():
    """
    Keep count of index was for debugging purposes.
    Looping through each element in line, checking if a possible number is written down.
    The catch: e.g. oneight -> how to capture overlapping numbers. And make sure that 'e' is used for eight
    after it has found one.
    """
    total_list_2 = []
    for i, line in enumerate(data):
        li = []
        word = ""
        match = False
        for char in line:
            if not char.isdigit():
                word += char
                for name, digit in dictionary.items():
                    if word == name:
                        li.append(str(digit))
                        word = char
                        match = True
                        break
                    elif name.startswith(word):
                        match = True
                        break
                    match = False
                if not match:
                    word = word[1:]
            else:
                li.append(char)
                word = ""
        pair = li[0] + li[-1]
        total_list_2.append(int(pair))
        # if total_list_2[i] != int(answers[i]):
        #     print(i)
    return sum(total_list_2)


total_2 = get_elem_from_data()
print("Answer Part 2: ", total_2)

from get_day_input import get_input
import math
import numpy as np

data = get_input(6).splitlines()
holding_button = data[0].split(':')[1].strip().split()
distance = data[1].split(':')[1].strip().split()
merged_list = list(zip(holding_button, distance))
list2 = []

for t, record in zip(holding_button, distance):
    count = 0
    maxi = int(t)/2
    winner = True
    possibilities = 0
    if int(t) % 2 == 0:
        while winner:
            new_d = (int(t) - maxi) * maxi
            if new_d < int(record):
                winner = False
            else:
                count += 1
            maxi += 1
        possibilities = (count*2) - 1
        list2.append(possibilities)
    else:
        maxi += 0.5
        while winner:
            new_d = (int(t) - maxi) * maxi
            if new_d < int(record):
                winner = False
            else:
                count += 1
            maxi += 1
        possibilities = (count * 2)
        list2.append(possibilities)

answer = np.prod(list2)
print("Part 1: ", answer)

data2 = ['Time:        7     15     30', 'Distance:   9   40   200']

t = data[0].split(':')[1].strip().split()
d = data[1].split(':')[1].strip().split()
new_t = "".join(t)
new_d = "".join(d)
print("t: ", new_t)
print("d: ", new_d)

pos_top = int(new_t) + math.sqrt((pow(int(new_t), 2) - 4*1*347152214061471))
neg_top = int(new_t) - math.sqrt((pow(int(new_t), 2) - 4*1*347152214061471))
bottom = 2
x1 = pos_top / bottom
x2 = neg_top / bottom
print(int(x1))
print(int(x2))
possible = x1 - x2
print("Part 2: ", int(possible))
from collections import deque


stacks = [deque() for i in range(9 + 1)]

with open("input.txt") as file:
    try:
        for line in file:
            for i in range(1, 9 + 1):
                current_element = line[1 + (4 * (i - 1))].strip()
                if current_element != "":
                    stacks[i].append(current_element)
    except IndexError:
        for i in range(1, len(stacks)):
            stacks[i].pop()
            stacks[i].reverse()
        for line in file:
            numbers = list(map(int, line.split()[1 : 5 + 1 : 2]))
            # print(numbers)
            movement_box = []
            for i in range(numbers[0]):
                movement_box.append(stacks[numbers[1]].pop())
            movement_box.reverse()
            for box in movement_box:
                stacks[numbers[2]].append(box)
            # for i in range(numbers[0]):
            #     stacks[numbers[2]].append(stacks[numbers[1]].pop())

for i in range(1, len(stacks)):
    stacks[i] = list(stacks[i])
    print(stacks[i][-1], end="")
print()

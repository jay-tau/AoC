import collections

with open("input.txt") as file:
    data = file.read()
    for i in range(len(data) - 4):
        count_dict = collections.Counter(data[i : i + 4])
        if len(count_dict) >= 4:
            print(i + 4)
            break

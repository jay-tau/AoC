import collections

with open("input.txt") as file:
    data = file.read()
    for i in range(len(data) - 14):
        count_dict = collections.Counter(data[i : i + 14])
        if len(count_dict) >= 14:
            print(i + 14)
            break

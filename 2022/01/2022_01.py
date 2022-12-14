max_sum = 0
sum_i = 0
with open("input.txt") as file:
    for line in file:
        if line == "\n":
            max_sum = max(sum_i, max_sum)
            sum_i = 0
        else:
            sum_i += int(line)
print(max_sum)

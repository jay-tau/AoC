max_sums = [0, 0, 0]
sum_i = 0
with open("input.txt") as file:
    for line in file:
        if line == "\n":
            if sum_i > min(max_sums):
                max_sums.remove(min(max_sums))
                max_sums.append(sum_i)
            sum_i = 0
        else:
            sum_i += int(line)
print(sum(max_sums))

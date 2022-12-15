count = 0
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        # print(line.split(","))
        l = []
        for cleaning_range in line.split(","):
            l.append(list(map(int, cleaning_range.split("-"))))
        # print(l)
        # break
        # For 0 in 1
        if l[0][0] >= l[1][0] and l[0][1] <= l[1][1]:
            count += 1
        # For 1 in 0
        elif l[1][0] >= l[0][0] and l[1][1] <= l[0][1]:
            count += 1
        # print(count)

print(count)

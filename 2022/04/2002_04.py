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
        if l[0][0] <= l[1][0] <= l[0][1] or l[0][0] <= l[1][1] <= l[0][1]:
            count += 1
        elif l[1][0] <= l[0][0] <= l[1][1] or l[1][0] <= l[0][1] <= l[1][1]:
            count += 1
        # print(count)

print(count)

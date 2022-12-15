score = 0
with open("input.txt") as file:
    for line in file:
        n = len(line)
        # print("Line:", line)
        d_1 = set(line[: n // 2])
        d_2 = set(line[n // 2 :])
        for common_element in d_1 & d_2:
            if "a" <= common_element <= "z":
                score += ord(common_element) - ord("a") + 1
            elif "A" <= common_element <= "Z":
                score += 26
                score += ord(common_element) - ord("A") + 1
            # print(common_element)
        # print(d_1)
        # print(d_2)
        # print("Score:", score)
        # break
print(score)

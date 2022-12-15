score = 0
with open("input.txt") as file:
    try:
        while 1:
            l_1 = set(file.readline().strip())
            l_2 = set(file.readline().strip())
            l_3 = set(file.readline().strip())
            # print(l_1, l_2, l_3)
            badge_element = list(l_1.intersection(l_2, l_3))[0]
            # print("badge_element", badge_element)
            if "a" <= badge_element <= "z":
                score += ord(badge_element) - ord("a") + 1
            elif "A" <= badge_element <= "Z":
                score += 26
                score += ord(badge_element) - ord("A") + 1
            # break
    except:
        pass
    finally:
        print(score)

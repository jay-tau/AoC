score = 0
with open("input.txt") as file:
    for line in file:
        opp_move = line[0]
        my_move = line[2]
        if my_move == "X":
            score += 1
            if opp_move == "C":
                score += 6
            elif opp_move == "A":
                score += 3
        elif my_move == "Y":
            score += 2
            if opp_move == "A":
                score += 6
            elif opp_move == "B":
                score += 3
        elif my_move == "Z":
            score += 3
            if opp_move == "B":
                score += 6
            elif opp_move == "C":
                score += 3
print(score)

score = 0
with open("input.txt") as file:
    for line in file:
        opp_move = line[0]
        direction = line[2]
        if direction == "X":
            score += 0
            if opp_move == "A":
                score += 3  # Z
            elif opp_move == "B":
                score += 1  # X
            elif opp_move == "C":
                score += 2  # Y
        elif direction == "Y":
            score += 3
            if opp_move == "A":
                score += 1  # X
            elif opp_move == "B":
                score += 2  # Y
            elif opp_move == "C":
                score += 3  # Z
        elif direction == "Z":
            score += 6
            if opp_move == "A":
                score += 2  # Y
            elif opp_move == "B":
                score += 3  # Z
            elif opp_move == "C":
                score += 1  # X

print(score)

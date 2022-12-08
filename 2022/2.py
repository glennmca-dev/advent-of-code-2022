# Day 2... messy but it works 😂
# rock paper scissors
oponents_moves = []
my_moves = []
my_scores_pt1 = []
my_scores_pt2 = []
oponent_a = 'rock'
oponent_b = 'paper'
oponent_c = 'scissors'
me_x = 'rock'
me_y = 'paper'
me_z = 'scissors'

# score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
rock = 1
paper = 2
scissors = 3
# plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
draw = 3
win = 6

def match_decision(oponent_move, my_move):
    if oponent_move == "rock":
        if my_move == "rock":
            return 'draw'
        if my_move == "paper":
            return 'win'
        if my_move == "scissors":
            return 'lose'
    if oponent_move == "paper":
        if my_move == "rock":
            return 'lose'
        if my_move == "paper":
            return 'draw'
        if my_move == "scissors":
            return 'win'
    if oponent_move == "scissors":
        if my_move == "rock":
            return 'win'
        if my_move == "paper":
            return 'lose'
        if my_move == "scissors":
            return 'draw'

def generate_score(my_move, result):
    score = 0
    if result == 'win':
        score += 6
    if result == 'draw':
        score += 3
    if my_move == 'rock':
        score += rock
    if my_move == 'paper':
        score += paper
    if my_move == 'scissors':
        score += scissors
    
    return score


with open("./2.txt", 'r') as f:
    lines = f.readlines()
    for i in lines:
        oponents_moves.append(i[0])
        my_moves.append(i[2])
    f.close()

def part_one():
    def play_game_part_one(oponent, me):
        oponent_move = ''
        my_move = ''
        if oponent == "A":
            oponent_move = oponent_a
        if oponent == "B":
            oponent_move = oponent_b
        if oponent == "C":
            oponent_move = oponent_c
        if me == "X":
            my_move = me_x
        if me == "Y":
            my_move = me_y
        if me == "Z":
            my_move = me_z
        decision = match_decision(oponent_move, my_move)
        score = generate_score(my_move, decision)
        my_scores_pt1.append(score)

    for i in range(len(my_moves)):
        play_game_part_one(oponents_moves[i], my_moves[i])

    def total_score(scores_list):
        score = 0
        for i in scores_list:
            score += i
        return score

    overall_score = total_score(my_scores_pt1)
    print(overall_score)

# part_one()

def part_two():
    x = 'lose'
    y = 'draw'
    z = 'win'
    moves = {
        "win" : {
            "rock" : "paper",
            "paper" : "scissors",
            "scissors" : "rock"
        },
        "draw" : {
            "rock" : "rock",
            "paper" : "paper",
            "scissors" : "scissors"
        },
        "lose" : {
            "rock" : "scissors",
            "paper" : "rock",
            "scissors" : "paper"
        }
    }
    def play_game_part_two(oponent, desired_result):
        if oponent == "A":
            oponent_move = oponent_a 
            # print(oponent_move) 
            if desired_result == "X":
                my_move = moves[x]['rock']
            if desired_result == "Y":
                my_move = moves[y]['rock']
            if desired_result == "Z":
                my_move = moves[z]['rock']
            # print(my_move)
        if oponent == "B":
            oponent_move = oponent_b 
            # print(oponent_move) 
            if desired_result == "X":
                my_move = moves[x]['paper']
            if desired_result == "Y":
                my_move = moves[y]['paper']
            if desired_result == "Z":
                my_move = moves[z]['paper']
            # print(my_move)
        if oponent == "C":
            oponent_move = oponent_c
            # print(oponent_move) 
            if desired_result == "X":
                my_move = moves[x]['scissors']
            if desired_result == "Y":
                my_move = moves[y]['scissors']
            if desired_result == "Z":
                my_move = moves[z]['scissors']
            # print(my_move)
        decision = match_decision(oponent_move, my_move)
        score = generate_score(my_move, decision)
        # print(decision, score)
        my_scores_pt2.append(score)
    
    # play_game_part_two("C", "Y")
    for i in range(len(my_moves)):
        play_game_part_two(oponents_moves[i], my_moves[i])

    def total_score(scores_list):
        score = 0
        for i in scores_list:
            score += i
        return score

    overall_score = total_score(my_scores_pt2)
    print(overall_score)

part_one()
part_two()
from aoc import day

input = day(8).splitlines()


def check_vis():
    visibility_counter = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if check_down(i,j,input[i][j]) or check_up(i,j,input[i][j]) or check_left(i,j,input[i][j]) or check_right(i,j,input[i][j]):
                visibility_counter +=1
    print(visibility_counter)


def check_down(ri, ci, height):
    if ri == len(input)-1:
        return True
    for i in input[ri+1:]:
        if i[ci] >= height:
            return False
    return True

def check_up(ri,ci,height):
    if ri == 0:
        return True
    for i in input[:ri]:
        if i[ci] >= height:
            return False
    return True

def check_left(ri, ci, height):
    if ci == 0: 
        return True
    left = input[ri][:ci]
    for i in left:
        if i >= height:
            return False
    return True

def check_right(ri, ci, height):
    if ci == len(input[ri]): 
        return True
    right = input[ri][ci+1:]
    for i in right:
        if i >= height:
            return False
    return True
    

def check_left2(ri, ci, height):
    if ci == 0: 
        return 0
    left = input[ri][:ci]
    left = left[::-1]
    counter = 0
    for i in left: #MIGHT NEED TO REVERSE THIS
        if i < height:
            counter += 1
        if i >= height:
            counter+=1
            return counter
    return counter
# def checkup2()

def check_up2(ri,ci,height):
    if ri == 0:
        return 0
    counter = 0
    for i in input[:ri][::-1]: # MIGHT NEED TO REVERSE THIS
        if i[ci] < height:
            counter +=1
        if i[ci] >= height:
            counter +=1
            return counter
    return counter


# def checkdown2()
def check_down2(ri, ci, height):
    if ri == len(input)-1:
        return 0
    counter = 0
    for i in input[ri+1:]:
        if i[ci] < height:
            counter +=1
        if i[ci] >= height:
            counter +=1
            return counter
    return counter


def check_right2(ri, ci, height):
    if ci == len(input[ri]): 
        return 0
    right = input[ri][ci+1:]
    counter = 0
    for i in right:
        if i < height:
            counter += 1
        if i >= height:
            counter+=1
            return counter
    return counter

def get_score(scores):
    score = scores[0] * scores[1] * scores[2] * scores[3]
    return score


total_scores = []
def scorefinder():
    for i in range(len(input)):
        for j in range(len(input[i])):
            tree_scores = []
            tree_scores.append(check_down2(i,j,input[i][j]))
            tree_scores.append(check_up2(i,j,input[i][j]))
            tree_scores.append(check_left2(i,j,input[i][j]))
            tree_scores.append(check_right2(i,j,input[i][j]))
            score = get_score(tree_scores)
            # print(tree_scores,i,j)
            total_scores.append(score)


scorefinder()
check_vis()
print(max(total_scores))
def diff_finder(input, unique):
    temp = ""
    for i in range(0,len(input)):
        if i > unique:
            temp = input[i-unique:i]
            pass_list = []
            for j in range(len(temp)):
                test = temp[j]
                if test not in temp[:j] and test not in temp[j+1:]:
                    pass_list.append(1)
                else: 
                    pass_list.append(0)
                if len(pass_list) == len(temp):
                    if 0 not in pass_list:
                        return i

def part_one():
    with open('./input.txt') as f:
        lines = f.readlines()
        for i in lines:
            answer = diff_finder(i, 4)
            print("answer = " + str(answer))

def part_two():
    with open('./input.txt') as f:
        lines = f.readlines()
        for i in lines:
            answer = diff_finder(i, 14)
            print("answer = " + str(answer))

part_one()
part_two()
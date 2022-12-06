import string
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

def getValue(input):
    if input.isupper():
        return upper.index(input)+27
    if input.islower():
        return lower.index(input)+1

def part_one():
    bags = {}
    duplicate_values = 0

    with open("./input.txt", 'r') as f:
        lines = f.readlines()
        for i in lines:
            i = i.strip('\n')
            # luckily all string in the list are an even length
            compartment1 = i[:len(i)//2]
            compartment2 = i[len(i)//2:]
            bags.update({i: {"comp1": compartment1, "comp2": compartment2}})
        f.close()


    for i in bags:
        for j in bags[i]['comp1']:
            if j in bags[i]['comp2']:
                duplicate_values += getValue(j)
                break

    print(duplicate_values)


def part_two():
    bag_groups = []
    group_values = 0

    with open("./input.txt", 'r') as f:
        lines = f.readlines()
        for i in range(0,len(lines),3):
            bags = [lines[i].strip('\n'), lines[i+1].strip('\n'), lines[i+2].strip('\n')]
            bag_groups.append(bags)
        f.close()

    for i in bag_groups:
        for j in i[0]:
            if j in i[1] and j in i[2]:
                group_values += getValue(j)
                break

    print(group_values)

part_one()
part_two()
def get_range(input):
    input = input.split('-')
    areas = list(range(int(input[0]), int(input[1])+1))
    return areas


# check if one range completely contains the other
def range_contains_whole_range(range1, range2):
    if range1[0] in range2 and range1[-1] in range2:
        return True
    if range2[0] in range1 and range2[-1] in range1:
        return True
    return False


# check if one range overlaps at all
def range_overlaps(range1, range2):
    for i in range1:
        if i in range2:
            return True
    return False


def part_one():
    with open('input.txt') as f:
        lines = f.readlines()
        counter = 0
        for line in lines:
            line = line.strip('\n').split(',')
            range1 = get_range(line[0])
            range2 = get_range(line[1])
            if range_contains_whole_range(range1, range2):
                counter += 1
        print(counter)


def part_two():
    with open('input.txt') as f:
        lines = f.readlines()
        counter = 0
        for line in lines:
            line = line.strip('\n').split(',')
            range1 = get_range(line[0])
            range2 = get_range(line[1])
            if range_overlaps(range1, range2):
                counter += 1
        print(counter)
    
    
part_one()
part_two()
def check_instruction(instruction):
    instruction = instruction.split(' ')
    amount = int(instruction[1])
    stack_from = int(instruction[3])
    stack_to = int(instruction[5])
    return amount, stack_from, stack_to


def top_of_stacks(stacks):
    result = ""
    for i in stacks:
        if stacks[i] != []:
            result += stacks[i][-1]
    print(result)

def part_one():
    stacks = {}
    indexes = []

    for i in range(1,10):
        stacks.update({f"stack{i}": []})

    def make_stacks(inputs):
        for i in inputs:
            line = i.strip('\n')
            for j in range(1,len(line),4):
                if line[j] != ' ':
                    if j in indexes:
                        stacks[f"stack{indexes.index(j)+1}"].append(line[j])
        for i in stacks:
            stacks[i].reverse()

    def move_from_stack(stack_from, stack_to, amount):
        for i in range(amount):
            stacks[f"stack{stack_to}"].append(stacks[f"stack{stack_from}"].pop())


    with open ('./5.txt') as f:
        lines = f.readlines()
        input_stacks = lines[:8]
        instructions = lines[10:]
        for i in range(1,len(input_stacks[0].strip('\n')),4):
            indexes.append(i)
        make_stacks(input_stacks)
        for i in instructions:
            amount, stack_from, stack_to = check_instruction(i)
            move_from_stack(stack_from, stack_to, amount)
        top_of_stacks(stacks)
        f.close()

def part_two():
    stacks = {}
    indexes = []

    def make_stacks(inputs):
        for i in inputs:
            line = i.strip('\n')
            for j in range(1,len(line),4):
                if line[j] != ' ':
                    if j in indexes:
                        stacks[f"stack{indexes.index(j)+1}"].append(line[j])
        for i in stacks:
            stacks[i].reverse()


    def move_from_stack2(stack_from, stack_to, amount):
        temp_list = []
        for i in range(amount):
            temp_list.append(stacks[f"stack{stack_from}"].pop())
        for i in range(len(temp_list)):
            stacks[f"stack{stack_to}"].append(temp_list.pop())

    for i in range(1,10):
        stacks.update({f"stack{i}": []})

    with open ('./5.txt') as f:
        lines = f.readlines()
        input_stacks = lines[:8]
        instructions = lines[10:]
        for i in range(1,len(input_stacks[0].strip('\n')),4):
            indexes.append(i)
        make_stacks(input_stacks)
        print()
        for i in instructions:
            amount, stack_from, stack_to = check_instruction(i)
            move_from_stack2(stack_from, stack_to, amount)
        top_of_stacks(stacks)
        f.close()

part_one()
part_two()

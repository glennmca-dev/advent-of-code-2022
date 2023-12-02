from aoc import day

input = day(10).splitlines()

split = []

for i in range(len(input)):
     split.append(input[i].split(' '))

x_val = 1
cycle = 0
cycle_val = {}

for i in split:
    cycle += 1
    cycle_val[cycle] = (x_val)
    if i[0] == 'addx':
        cycle +=1
        cycle_val[cycle] = (x_val)
        x_val += int(i[1])
        cycle_val[cycle] = (x_val)


val_steps = [20,60,100,140,180,220]
results = []
for i in val_steps:
    results.append(cycle_val[i-1])

def gen_score():
    scores = 0
    for i in val_steps:
        print(f"Cycle: {str(i)}, X value: {str(cycle_val[i])},")
        # scores += cycle_val[i-1][0] * cycle_val[i-1][1]
    return scores

scores = gen_score()
print(scores)
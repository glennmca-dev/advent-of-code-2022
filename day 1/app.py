elf_total = []
highest_score = 0


with open("./input.txt", 'r') as f:
    elf_calories = 0
    lines = f.readlines()
    for i in lines:
        if i == '\n':
            elf_total.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(i.strip('\n'))
    f.close()


for i in elf_total:
    if i > highest_score:
        highest_score = i


elf_total.sort()
highest_score = elf_total[-1]
print(highest_score)

# End of part one 
# part 2

top_three_elves = [elf_total[-1], elf_total[-2], elf_total[-3]]
top_three_sum = 0
for i in top_three_elves:
    top_three_sum += i
    

print(top_three_elves)
print(top_three_sum)

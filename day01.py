with open("/Users/arun.yusuf/PycharmProjects/advent_of_code_2022/day01_input.txt") as d:
    d_str = d.read()
    d_list = d_str.split("\n")

sub_total = 0
cals_per_elf = []

for cals in d_list:
    if cals == "":
        cals_per_elf.append(sub_total)
        sub_total = 0
    else:
        sub_total += int(cals)

# answer to problem 1.1
answer_1 = max(cals_per_elf)

cals_per_elf.sort(reverse=True)
cals_top_3 = 0
for i in range(3):
    cals_top_3 += cals_per_elf[i]

# answer to problem 1.2
answer_2 = cals_top_3

print(answer_1)
print(answer_2)
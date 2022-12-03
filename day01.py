def day_01():
    with open("/Users/arun.yusuf/PycharmProjects/advent_of_code_2022/day01_input.txt") as d:
        d_list = d.read().split("\n")

    sub_total = 0
    cals_per_elf = [sub_total := sub_total + int(x) if x != "" else (sub_total := 0) for x in d_list]

    answer_1 = max(cals_per_elf)

    cals_per_elf.sort(reverse=True)

    answer_2 = sum(cals_per_elf[0:3])

    return answer_1, answer_2

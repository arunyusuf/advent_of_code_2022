def day_04():
    with open("/Users/arun.yusuf/PycharmProjects/advent_of_code_2022/day_04_input.txt") as d:
        d_list = d.read().split("\n")

    answer_1 = 0
    answer_2 = 0

    for elf_pair in d_list:
        elf_one, elf_two = elf_pair.split(",")
        elf_one_low, elf_one_high = elf_one.split("-")
        elf_two_low, elf_two_high = elf_two.split("-")

        if int(elf_one_low) >= int(elf_two_low) and int(elf_one_high) <= int(elf_two_high):
            answer_1 += 1
        elif int(elf_two_low) >= int(elf_one_low) and int(elf_two_high) <= int(elf_one_high):
            answer_1 += 1

        if int(elf_one_high) >= int(elf_two_low) and int(elf_one_low) <= int(elf_two_high):
            answer_2 += 1
        elif int(elf_two_high) >= int(elf_one_low) and int(elf_two_low) <= int(elf_one_high):
            answer_2 += 1

    return answer_1, answer_2

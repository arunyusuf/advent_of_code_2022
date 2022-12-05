def day_03():
    with open("/Users/arun.yusuf/PycharmProjects/advent_of_code_2022/day_03_input.txt") as d:
        d_list = d.read().split("\n")

    answer_1 = 0
    answer_2 = 0
    counter = 0

    for ruck in d_list:
        skip = ""
        counter += 1
        for char in ruck[len(ruck)//2:]:
            if char in ruck[:len(ruck)//2]:
                if char not in skip:
                    if ord(char) > 96:
                        answer_1 += ord(char) - 96
                        skip += char
                    else:
                        answer_1 += ord(char) - 38
                        skip += char
        if counter == 1:
            elf_one = ruck
        if counter == 2:
            elf_two = ruck
        if counter == 3:
            for char in ruck:
                if char in elf_one and char in elf_two:
                    if ord(char) > 96:
                        answer_2 += ord(char) - 96
                    else:
                        answer_2 += ord(char) - 38
                    break
            counter = 0

    return answer_1, answer_2

import copy

def day_05():
    with open("/Users/arun.yusuf/PycharmProjects/advent_of_code_2022/day_05_input.txt") as d:
        d_list = d.read().split("\n")

    answer_1 = ""
    answer_2 = ""

    stacks = {}

    for line in d_list:
        if "[" in line:
            char_counter = 0
            for char in line:
                char_counter += 1
                if (char_counter + 2) % 4 == 0 and char != " ":
                    stack = str((char_counter + 2) // 4)
                    if stack in stacks.keys():
                        stacks[stack].insert(0, char)
                    else:
                        stacks[stack] = [char]

    # for answer 2
    stacks_v2 = copy.deepcopy(stacks)

    for line in d_list:
        if "move" in line:
            word_list = line.split()
            n_o_d = [word for word in word_list if word.isdecimal()]
            number = int(n_o_d[0])
            origin = n_o_d[1]
            destination = n_o_d[2]

            # answer 1 logic
            for i in range(number):
                crate = stacks[origin].pop()
                stacks[destination].append(crate)

            # answer 2 logic
            crates = stacks_v2[origin][-number:]
            stacks_v2[destination].extend(crates)
            stacks_v2[origin] = stacks_v2[origin][:-number]

    keys = list(stacks.keys())
    keys.sort()
    for stack in keys:
        answer_1 += stacks[stack][-1]
        answer_2 += stacks_v2[stack][-1]

    return answer_1, answer_2


def day_02():
    with open("/Users/arun.yusuf/PycharmProjects/advent_of_code_2022/day02_input.txt") as d:
        d_list = d.read().lower().split("\n")

    answer_1 = 0
    answer_2 = 0

    for rps_round in d_list:
        if rps_round[2] == "x":
            if rps_round[0] == "a":
                answer_1 += 4
                answer_2 += 3
            if rps_round[0] == "b":
                answer_1 += 1
                answer_2 += 1
            if rps_round[0] == "c":
                answer_1 += 7
                answer_2 += 2
        if rps_round[2] == "y":
            if rps_round[0] == "a":
                answer_1 += 8
                answer_2 += 4
            if rps_round[0] == "b":
                answer_1 += 5
                answer_2 += 5
            if rps_round[0] == "c":
                answer_1 += 2
                answer_2 += 6
        if rps_round[2] == "z":
            if rps_round[0] == "a":
                answer_1 += 3
                answer_2 += 8
            if rps_round[0] == "b":
                answer_1 += 9
                answer_2 += 9
            if rps_round[0] == "c":
                answer_1 += 6
                answer_2 += 7

    return answer_1, answer_2


def day_02_v2():
    with open("/Users/arun.yusuf/PycharmProjects/advent_of_code_2022/day02_input.txt") as d:
        d_list = d.read().lower().split("\n")

    scores = {
        "a": {
            "x": (4, 3),
            "y": (8, 4),
            "z": (3, 8)
        },
        "b": {
            "x": (1, 1),
            "y": (5, 5),
            "z": (9, 9)
        },
        "c": {
            "x": (7, 2),
            "y": (2, 6),
            "z": (6, 7)
        }
    }

    answer_1 = 0
    answer_2 = 0

    for rps_round in d_list:
        answer_1 += scores[rps_round[0]][rps_round[2]][0]
        answer_2 += scores[rps_round[0]][rps_round[2]][1]

    return answer_1, answer_2
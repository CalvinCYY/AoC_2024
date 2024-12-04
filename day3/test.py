import re


def get_input():
    with open("input-3.txt") as f:
        inp = f.read()

    return inp


def part1():
    inp = get_input()
    muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inp)
    sums = 0
    for mul in muls:
        sums += int(mul[0]) * int(mul[1])

    print(sums)


def part2():
    inp = get_input()
    muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)", inp)
    sums = 0
    enabled = True
    for mul in muls:
        if enabled and mul[0] != "" and mul[1] != "":
            sums += int(mul[0]) * int(mul[1])
        else:
            if mul[2] == "do":
                enabled = True
            else:
                enabled = False
    print(sums)


if __name__ == "__main__":
    part1()
    part2()

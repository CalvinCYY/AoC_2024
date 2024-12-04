def get_input():
    with open("input-4.txt") as f:
        grid = []
        for line in f:
            grid.append(line.strip())

    return grid


def solve(data, slices, variants):
    count = 0

    for x in range(len(data[0])):
        for y in range(len(data)):
            for slice in slices:
                try:
                    word = "".join([data[y + dY][x + dX] for dX, dY in slice])

                    if any(word == variant for variant in variants):
                        count += 1
                except:
                    pass

    return count


def part1():

    slices1 = [
        [[0, 0], [1, 0], [2, 0], [3, 0]],
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 1], [2, 2], [3, 3]],
        [[0, 3], [1, 2], [2, 1], [3, 0]],
    ]

    return solve(get_input(), slices1, ["XMAS", "SAMX"])


def part2():
    slices2 = [
        [[0, 0], [1, 1], [2, 2], [0, 2], [1, 1], [2, 0]],
    ]

    return solve(get_input(), slices2, ["MASMAS", "SAMSAM", "MASSAM", "SAMMAS"])


if __name__ == "__main__":
    print(part1())
    print(part2())

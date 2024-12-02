def get_input():
    with open("input.txt") as f:
        reports = []
        for line in f:
            level = line.split()
            for i in range(len(level)):
                level[i] = int(level[i])
            reports.append(level)

    return reports


# part1


def get_safe(safe_limit=3):
    reports = get_input()
    safe = 0

    for level in reports:
        level_safe = True
        diff_up = None
        diff_down = None

        for i in range(len(level) - 1):
            if not level_safe:
                continue

            diff = level[i] - level[i + 1]
            next_diff_abs = abs(diff)

            if diff > 0:
                diff_up = diff

            if diff < 0:
                diff_down = diff

            if diff_up and diff_down or not (1 <= next_diff_abs <= safe_limit):
                level_safe = False

        if level_safe:
            safe += 1

    return safe


# part2


def check_level(level, safe_limit=3):
    diff_up = None
    diff_down = None

    for i in range(len(level) - 1):
        diff = level[i] - level[i + 1]
        next_diff_abs = abs(diff)

        if diff > 0:
            diff_up = diff

        if diff < 0:
            diff_down = diff

        if diff_up and diff_down or not (1 <= next_diff_abs <= safe_limit):
            return False

    return True


def get_dampner():
    reports = get_input()
    safe = 0

    for level in reports:
        check = check_level(level)
        if not check:
            for i in range(len(level)):
                # this is super inefficient but it works
                temp_level = level.pop(i)
                if check_level(level):
                    check = True
                    break
                level.insert(i, temp_level)

        if check:
            safe += 1

    return safe


if __name__ == "__main__":
    print(get_safe())
    print(get_dampner())

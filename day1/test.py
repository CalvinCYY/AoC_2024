from collections import Counter


def get_input():
    with open("input.txt", "r") as f:
        list1 = []
        list2 = []
        for line in f:
            line = line.split()
            list1.append(int(line[0]))
            list2.append(int(line[1]))

    list1.sort()
    list2.sort()

    return list1, list2


# part 1
def get_diff():
    list1, list2 = get_input()

    total_diff = 0
    for i in range(len(list1)):
        total_diff += abs(list1[i] - list2[i])

    return total_diff


# part 2
def get_similarity():
    list1, list2 = get_input()

    dict2 = Counter(list2)
    similarity_score = 0

    for i in list1:
        similarity_score += i * dict2[i]

    return similarity_score


if __name__ == "__main__":
    print(get_diff())
    print(get_similarity())

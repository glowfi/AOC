from types import new_class


def isIncreasing(level: list[int]) -> bool:
    for i in range(1, len(level)):
        if level[i] > level[i - 1] and 1 <= level[i] - level[i - 1] <= 3:
            continue
        else:
            return False
    return True


def isDecreasing(level: list[int]) -> bool:
    for i in range(1, len(level)):
        if level[i] < level[i - 1] and 1 <= abs(level[i] - level[i - 1]) <= 3:
            continue
        else:
            return False
    return True


def part1(mat: list[list[int]]) -> int:
    levelsSafe = 0
    for i in range(len(mat)):
        if isIncreasing(mat[i]) or isDecreasing(mat[i]):
            levelsSafe += 1

    return levelsSafe


def part2(mat: list[list[int]]) -> int:
    levelsSafe = 0
    for i in range(len(mat)):
        if isIncreasing(mat[i]) or isDecreasing(mat[i]):
            levelsSafe += 1
        else:
            for removeIdx in range(len(mat[i])):
                newLevel = mat[i][:removeIdx] + mat[i][removeIdx + 1 :]
                if isIncreasing(newLevel) or isDecreasing(newLevel):
                    levelsSafe += 1
                    break

    return levelsSafe


matrix: list[list[int]] = []

with open("./input.txt") as fp:
    rows = fp.readlines()
    for row in rows:
        row = row.strip("").strip("\n")
        matrix.append([int(x) for x in row.split(" ")])

print(part1(matrix))
print(part2(matrix))

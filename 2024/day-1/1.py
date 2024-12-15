from collections import defaultdict


def part1(leftList: list[int], rightList: list[int]) -> int:
    dist = 0
    for leftSmallest, rightSmallest in zip(sorted(leftList), sorted(rightList)):
        diff = abs(rightSmallest - leftSmallest)
        dist += diff

    return dist


def part2(leftList: list[int], rightList: list[int]):
    countMap = defaultdict(int)
    similarityScore = 0

    for numL in leftList:
        for numR in rightList:
            if numR == numL:
                countMap[numR] += 1
        similarityScore += numL * countMap[numL]

    return similarityScore


leftList: list[int] = []
rightList: list[int] = []

with open("input.txt") as fp:
    rows = fp.readlines()
    for row in rows:
        row = row.strip("").strip("\n").split("   ")
        if len(row) == 2:
            a, b = row
            leftList.append(int(a))
            rightList.append(int(b))

print(part1(leftList, rightList))
print(part2(leftList, rightList))

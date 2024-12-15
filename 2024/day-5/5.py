from collections import defaultdict


def isOrderedMaintained(
    val: int, arr: list[int], pagePrintOrder: dict[int, list[int]]
) -> bool:
    for v in arr:
        if v in pagePrintOrder and any(x == val for x in pagePrintOrder[v]):
            return False
    return True


def part1(pagePrintOrder: dict[int, list[int]], res: list[list[int]] = []) -> int:
    sm = 0
    for result in res:
        isOrderMaintained = False
        for idx, val in enumerate(result):
            if not isOrderedMaintained(val, result[idx + 1 :], pagePrintOrder):
                isOrderMaintained = False
                break
            else:
                isOrderMaintained = True
        if isOrderMaintained:
            midIdx = len(result) // 2
            sm += result[midIdx]
    return sm


def part2(pagePrintOrder: dict[int, list[int]], res: list[list[int]] = []) -> int:
    sm = 0
    for result in res:
        isOrderMaintained = False
        for idx, val in enumerate(result):
            if not isOrderedMaintained(val, result[idx + 1 :], pagePrintOrder):
                isOrderMaintained = False
                break
            else:
                isOrderMaintained = True
        if not isOrderMaintained:
            newResult = []

            midIdx = len(newResult) // 2
            sm += newResult[midIdx]
    return sm


pagePrintOrder: dict[int, list[int]] = defaultdict(list)
res: list[list[int]] = []
with open("./input.txt") as fp:
    data = fp.readlines()

    resIdx = 0
    for row in data:
        if row.strip(" ").strip("\n") == "":
            break
        else:
            a, b = row.strip(" ").strip("\n").split("|")
            print(a, b)
            pagePrintOrder[int(a)].append(int(b))
            resIdx += 1

    for row in data[resIdx + 1 :]:
        res.append([int(x) for x in row.strip("").strip("\n").split(",")])

print(part1(pagePrintOrder, res))
print(part2(pagePrintOrder, res))

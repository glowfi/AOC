def hasXmas1(i: int, j: int, board: list[list[str]], dirVec: tuple[int, int]) -> bool:
    idx = 1
    initialPosition = [i, j]
    while idx < 4:
        initialPosition[0] += dirVec[0]
        initialPosition[-1] += dirVec[-1]
        x, y = initialPosition[0], initialPosition[-1]

        if x < 0 or x >= len(board):
            return False
        if y < 0 or y >= len(board[0]):
            return False

        if board[x][y] != "XMAS"[idx]:
            return False
        idx += 1
    return True


def part1(board: list[list[str]]):
    c = 0
    dirs = [(1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1), (-1, 0), (0, -1)]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "X":
                for dirVec in dirs:
                    if hasXmas1(i, j, board, dirVec):
                        c += 1
    return c


def inBounds(x: int, y: int, board: list[list[str]]) -> bool:
    if x < 0 or x >= len(board):
        return False
    if y < 0 or y >= len(board[0]):
        return False
    return True


def hasXmas2(i: int, j: int, board: list[list[str]]):
    dirs = [
        (-1, -1),
        (1, -1),
        (-1, 1),
        (1, 1),
    ]
    countMap = {"M": 0, "S": 0}

    # Nw and Se corners
    nw_x = i + dirs[0][0]
    nw_y = j + dirs[0][-1]

    sw_x = i + dirs[1][0]
    sw_y = j + dirs[1][-1]

    if not inBounds(nw_x, nw_y, board) or not inBounds(sw_x, sw_y, board):
        return False

    if board[nw_x][nw_y] not in "MS" or board[sw_x][sw_y] not in "MS":
        return False

    countMap[board[nw_x][nw_y]] += 1
    countMap[board[sw_x][sw_y]] += 1

    # Sw and Ne corners
    ne_x = i + dirs[2][0]
    ne_y = j + dirs[2][-1]

    se_x = i + dirs[3][0]
    se_y = j + dirs[3][-1]

    if not inBounds(ne_x, ne_y, board) or not inBounds(se_x, se_y, board):
        return False

    if board[ne_x][ne_y] not in "MS" or board[se_x][se_y] not in "MS":
        return False

    countMap[board[ne_x][ne_y]] += 1
    countMap[board[se_x][se_y]] += 1

    if board[nw_x][nw_y] == board[se_x][se_y] or board[ne_x][ne_y] == board[sw_x][sw_y]:
        return False

    for _, v in countMap.items():
        if v != 2:
            return False

    return True


def part2(board: list[list[str]]):
    c = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "A":
                if hasXmas2(i, j, board):
                    c += 1
    return c


board: list[list[str]] = []
with open("./input.txt") as fp:
    for row in fp.readlines():
        board.append([x for x in row])


print(part1(board))
print(part2(board))

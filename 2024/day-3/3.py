import re


def part1(txt):
    pat = re.compile(r"mul\((\d+),(\d+)\)")
    res = pat.findall(txt)
    sm = 0
    for mul in res:
        sm += int(mul[0]) * int(mul[1])
    return sm


def part2(txt):
    pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"
    instructions = re.finditer(pattern, "".join(txt))

    enabled = True
    result = 0

    for inst in instructions:
        inst = inst.groups()
        match inst[0]:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _ if enabled:
                result += int(inst[1]) * int(inst[2])

    return result


txt = ""
with open("./input.txt") as fp:
    txt = fp.read()

print(part1(txt))
print(part2(txt))

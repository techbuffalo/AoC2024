#AoC Day 2 2024 - Noah Duran
import re

with open("input.txt") as fileInput:
    reports = fileInput.read().strip().split("\n")

testReport = [list(map(int, re.findall("\\d+", x))) for x in reports]

def part1(levels):
    return all(1 <= abs(n1 - n2) <= 3 for n1, n2 in zip(levels, levels[1:])) and (
        levels == sorted(levels) or levels == sorted(levels)[::-1]
    )


def part2(levels):
    return any(part1(levels[:i] + levels[i+1:]) for i in range(len(levels)))


print(sum(part1(testReport) for levels in testReport))
print(sum(part2(testReport) for levels in testReport))


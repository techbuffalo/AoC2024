#Advent of Code Day 3 2024 Noah Duran
import re

with open("input.txt") as inputFile:
    instructions = inputFile.read()


def part1(input):
    #Looks through input and finds all mul(num, num) matches then gets running total of all products
    pattern = r"mul\([0-9,]+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, instructions)

    total = 0
    goodLines = False
    for line in matches:
        if "do(" in line:
            goodLines = True
        elif "don't(" in line:
            goodLines = False
        elif "mul(" in line and goodLines:
            print(line)
            numbers = line[4:-1].split(',')
            if len(numbers) >= 2:
                num1 = numbers[0]
                num2 = numbers[1]
                total += (int(num1) * int(num2))

    print(total)

part1(instructions)
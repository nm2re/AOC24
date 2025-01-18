import re

with open('../inputs/day3input.txt') as file:
    input_file = file.read()

    mul_pattern = r'mul\(-?\d+,-?\d+\)'
    combined_pattern = re.compile(r'do\(\)|don\'t\(\)|mul\(-?\d+,-?\d+\)')

    multiplication = True # if multiplication is enabled or disabled
    total = 0
    matches = re.findall(combined_pattern, input_file)

    for match in matches:
        if match == "do()":
            multiplication = True
        elif match == "don't()":
            multiplication = False

        numbers = re.findall(r'\d+', match)
        if numbers and multiplication:
            num1,num2 = map(int, numbers)
            total += num1 * num2

    print(total)
import re

with open('../inputs/day3input.txt', 'r') as file:
    input_file = file.read()
    pattern = r'mul\(-?\d+,-?\d+\)'

    total = 0
    matches = re.findall(re.compile(pattern), input_file)
    for item in matches:
        # remove func name
        numbers = re.findall(r'\d+', item)
        num1, num2 = map(int,numbers)
        total += (int(num1) * int(num2))
    print(total)



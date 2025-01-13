import re

with open('inputs/day3test.txt') as file:
    input_file = file.read()
    print(input_file)

    # regex of do()
    enable_function = r'do()'
    disable_function = r"don't()"
    mul_pattern = r'mul\(-?\d+,-?\d+\)'

    combined_pattern = re.compile(r'do\(\)|don\'t\(\)|mul\(-?\d+,-?\d+\)')

    matches = re.findall(combined_pattern, input_file)
    print(matches)

    i = 1
    disable_numbers = 0
    total = 0
    for i in range(len(matches) - 1):

        total_numbers = re.findall(r'\d+', matches[i])
        num1, num2 = map(int, total_numbers)
        total+= (num1 * num2)
        print(total)

        if matches[i-1] == disable_function:
            numbers = re.findall(stripping, matches[i])
            num1, num2 = map(int, numbers)
            disable_numbers += (num1 * num2)
            print(disable_numbers)






    # regex of don't()

# with open("inputs/day2input.txt","r") as file:
#
#     input_file = file.read().splitlines()
#
#     count = 0
#     for line in input_file:
#
#         line = line.split(' ')
#         checkAscending = None
#
#         for i in range(len(line) - 1):
#             if (checkAscending is None or (int(line[i]) < int(line[i + 1]) and checkAscending) or (int(line[i]) > int(line[i + 1]) and not checkAscending)) and (1 <= abs(int(line[i]) - int(line[i + 1])) <= 3):
#                 checkAscending = int(line[i]) < int(line[i + 1])
#             else:
#
#                 break
#         else:
#             count+=1

# print(count)


def check_valid(array):
    diff = []
    for i in range(len(array) - 1):
        diff.append((array[i] - array[i + 1]))

    if (all(x > 0 and x in range(0,4) for x in diff)) or (all(x < 0 and x in range(-3,0) for x in diff)):
        return True
    else:
        return False


with open('inputs/day2input.txt', 'r') as file:
    input_data = file.readlines()

    count = 0
    for line in input_data:
        numbers = [int(num.strip()) for num in line.split()] # one list one row of numbers

        if check_valid(numbers):
            count+=1

    print(count)


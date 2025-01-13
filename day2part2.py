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

    count = 0 # now counts safe + unsafe changed into safe
    for line in input_data:
        numbers = [int(num.strip()) for num in line.split()] # one list one row of numbers

        if check_valid(numbers):
            count+=1
        else:
            for i in range(len(numbers)):
                temp_numbers = numbers.copy()
                temp_numbers.pop(i)

                if check_valid(temp_numbers):
                    count+=1
                    break

    print(count)

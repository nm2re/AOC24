with open('../inputs/day4test.txt', 'r') as file:
    input_file = file.read()

    grid = [list(row) for row in input_file.split('\n')]

    word = 'XMAS'
    reversed_word = word[::-1]
    count = 0

    def check_string(_string):
        return _string.count(word) + _string.count(reversed_word)


    # horizontal calculation

    for row in grid:
        print(row)
        count += check_string(''.join(row))


    # vertical calculation

    for i in range(len(grid)):
        count += check_string(''.join(grid[j][i] for j in range(len(grid[0]))))


    # diagonal calculation

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i <= len(grid) - 4 and j <= len(grid[0]) - 4:
                    count += check_string(''.join(grid[i+k][j+k] for k in range(4)))



    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i <= len(grid) - 4 and j >= 3:
                    count += check_string(''.join(grid[i+k][j-k] for k in range(4)))



    print(count)
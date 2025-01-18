file = open('../inputs/day1input.txt', 'r')


input_file = file.read().split('\n')

list1 = []
list2 = []

for line in input_file:
    num1,num2 = line.split()
    list1.append(int(num1))
    list2.append(int(num2))

_sum = 0

for i in range(len(list1)):
    _sum += list1[i] * list2.count(list1[i])


print(_sum)

    # number * times in second list
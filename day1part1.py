

file = open("inputs/day1input.txt","r")

input_file = file.read().split('\n')

list1 = []
list2 = []

for line in input_file:
    num1,num2 = line.split()
    list1.append(int(num1))
    list2.append(int(num2))

list1.sort()
list2.sort()
sum = 0
for i in range(len(list1)):
    sum+= abs(list1[i] - list2[i])

print(sum)

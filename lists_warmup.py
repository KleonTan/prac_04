numbers = [3, 1, 4, 1, 5, 9, 2]
numbers2 = []


numbers[0] = 10
print(numbers)
numbers[-1] = 1
print(numbers)
for i in range(-5, 0, 1):
    numbers2.append(numbers[i])
    print(i)
print(numbers2)

if 9 in numbers:
    print(True)
else:
    print(False)

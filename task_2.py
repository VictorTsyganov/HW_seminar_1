# Вывести все простые числа от 1 до 1000 

simple_numbers = []

for i in range(1, 1001):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            simple_numbers.append(i)

print(simple_numbers)
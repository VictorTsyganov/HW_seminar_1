# Вычислить n-ое треугольного число(сумма чисел от 1 до n), n!
# (произведение чисел от 1 до n)

n = int(input('Введите число '))

sum_to_n = 1
mult_to_n = 1

for i in range(2, n + 1):
    sum_to_n += i
    mult_to_n *= i

print(f'Cумма чисел от 1 до {n} равна {sum_to_n}')
print(f'Произведение чисел от 1 до {n} равна {mult_to_n}')

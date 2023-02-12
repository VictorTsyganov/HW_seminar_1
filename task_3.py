# Реализовать простой калькулятор

n = input('Введите операцию с 2-умя числами(без пробелов) на простом калькуляторе (+, -, *, /) и нажмите enter ')

if n.find('+') > 0:
    new_list = list(map(float, n.split('+')))
    print(new_list[0] + new_list[1])

if n.find('*') > 0:
    new_list = list(map(float, n.split('*')))
    print(new_list[0] * new_list[1])

if n.find('-') > 0:
    new_list = list(map(float, n.split('-')))
    print(new_list[0] - new_list[1])

if n.find('/') > 0:
    new_list = list(map(float, n.split('/')))
    print(new_list[0] / new_list[1])

# Задано уравнение вида q + w = e, q, w, e >= 0. Некоторые цифры
# могут быть заменены знаком вопроса, например 2? + ?5 = 69. Требуется
# восстановить выражение до верного равенства. Предложить хотя бы
# одно решение или сообщить, что его нет.

n = input('Запиште уравнение с использованием знаков вопроса ')
new_n = n.replace(' ', '')
if new_n.find('+') > 0:
    s = new_n.split('=')
    new_list = s[0].split('+')
    new_list.append(s[1])
    list_solutions = []
    for i in range(0, 10):
        q = int(new_list[0].replace('?', str(i)))
        for j in range(0, 10):
            w = int(new_list[1].replace('?', str(j)))
            for k in range(0, 10):
                e = int(new_list[2].replace('?', str(k)))
                if q + w == e:
                    list_solutions.append(f'{str(q)} + {str(w)} = {str(e)}')
    if list_solutions:
        print('Перечень возможных решений: ')
        for item in set(list_solutions):
            print(item)
    else:
        print('Заданное уравнение не имеет решений!')

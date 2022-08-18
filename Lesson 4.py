# задание 1

def my_func():
    a = float(input('Введите количество отработанных часов : '))
    b = float(input('Введите суммы оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = a * b
    return pay + c
print(f'Размер заработной платы составил: {my_func() }')


# задание 2

my_list = [15, 2, 3, 1, 7, 5, 4, 10]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')




# задание 3

print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')


# задание 4


my_list = [2, 10, 4, 4, 6, 9, 9, 1, 78, 3, 5]
res = [i for i in my_list if my_list.count(i) == 1]
print(res)

# задание 5

from functools import reduce

list = [i for i in range(100, 1001, 2)]
print("Список чётных чисел в диапазоне [100..1000]:\n", list)
print("Произведение всех элементов списка:\n", reduce(lambda x,y: x*y, list))


# задание 6

from itertools import count

for el in count(int(input('Введите стартовое число '))):
    print(el)


from itertools import cycle

list = [5, 1, 8, 55, 3, 8, 9, 2, 4, 11, 99]
for i in cycle(list):
    print(i, end=' ')

# задание 7

from math import factorial

def my_func_3(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)

print("<<Программа вычисления факториала числа>>")
for el in factorial_gen(15):
    print(el)







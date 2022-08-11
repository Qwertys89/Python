# задание 1

my_list= [-45, 38, 4.6, None, 'text', ]
for i in my_list:
    print(f'{i} is {type(i)}')

# задание 2

elements= int(input("Введите количество элементов списка"))
my_list =[]
i=0
element=0
while i<elements:
    my_list.append(input("Введите значение списка"))
    i+=1
for a in range(int(len(my_list)/2)):
    my_list[element], my_list[element+1]=my_list[element+1], my_list[element]
    element+=2
print(my_list)

# задание 3

number = int(input("Введите номер месяца: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'Зима', 2: 'Весна',3: 'Весна',4: 'Весна',5: 'Весна',6: 'Лето',7: 'Лето',8: 'Лето',9: 'Осень',10: 'Осень',11: 'Зима',12: 'Зима'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Месяц относится к {month_list[i]}")
            break
    print(f"Месяц относится к {month_dict[number]}")
else:
    print("Такого месяца не существует")

# задание 4

my_str=input("Введите строку:")
b=my_str.split(' ')
for i, element in enumerate(b, 1):
    if len(element)>10:
        element=element[0:10]
    print(f"{i}. {element}")

# задание 5

my_list = [7, 5, 3, 3, 2]
number = int(input("Введите число: "))
a=my_list.count(number)
for element in my_list:
    if a>0:
        i=my_list.index(number)
        my_list.insert(i, number)
        break
    else:
        if number>element:
            b=my_list.index(element)
            my_list.insert(b, number)
            break
        elif number < my_list[len(my_list)-1]:
            my_list.append(number)
print(my_list)

# задание 6

goods = []
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 1
while True:
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    unit = input('Введите единицу измерения товара: ')
    params = {'name': name,'price': price,'quantity': quantity,'unit': unit}
    good = (num, params)
    goods.append(good)

    for key, value in params.items():
        i = analytics.get(key)
        if value in i:
            continue
        i.append(value)
        continue

    num += 1
    exit_answer = input('Ввести еще позицию? ').lower()
    if exit_answer == 'нет':
        break
print(analytics)


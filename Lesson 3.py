# задание 1

def my_function(a,b):
    try:
        c=a/b
        return c
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
print(my_function(int(input('Введите первое число: ')), int(input('Введите второе число: '))))


# задание 2

def second_func(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)
second_func(name='Vova', surname='Petrov', year='1989', city='Moscow', email='PetrovVS@', phone='1234')

# задание 3

def my_func(a1,a2,a3):
    if a1>a3 and a2>a3:
       return a1+a2
    elif a1>a2 and a1<a3:
       return a1+a3
    else:
        return a2+a3
print(my_func(int(input('Введите первый аргумент: ')), int(input('Введите второй аргумент: ')), int(input('Введите третий аргумент: '))))


# задание 4

def my_func1(x,y):
    return x**y
print(my_func1(int(input('Введите действительное положительное число x: ')), int(input(' Введите целое отрицательное число y: '))))


def my_func2(x,y):
    counter = 1
    result = 1/x
    while counter<abs(y):
        result=result*(1/x)
        counter+=1
    return result
print(my_func2(int(input('Введите действительное положительное число x: ')), int(input(' Введите целое отрицательное число y: '))))


# задание 5

def my_func3():
    sum=0
    a=False
    while not a:
        numbers=input('Введите числа или нажмите z для выхода: ').split()
        result=0
        for i in range(len(numbers)):
            if numbers[i]=='z':
                a=True
                break
            else:
                result+=int(numbers[i])
        sum+=result
        print(sum)

my_func3()


# задание 6

def int_func():
    word=input('Введите слова: ')
    return word.title()

print(int_func())

# задание 7

def my_func(a):
    separate_word = a.split(' ')
    total = []
    for i in separate_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total
print(my_func("hello world"))











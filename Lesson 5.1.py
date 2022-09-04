# задание 1

with open('new_file.txt', 'a') as file:
    while True:
        a=input('Введите текст: ')
        file.write(a + '\n')
        if not a:
            break

















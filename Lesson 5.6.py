# задание 6

def subjects():
    try:

        mydict = {}
        with open("file_6.txt", encoding='utf-8') as fobj:
            for line in fobj:
                name, stats = line.split(':')
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))

                mydict[name] = name_sum
            print(f"{mydict}")
    except FileNotFoundError:
        return 'Файл не найден.'


subjects()
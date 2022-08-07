# 1 задание

a=1032
b=33
c=10
print(a,b,c)


a=int(input("Введите число:"))
print(a)
b=(input("Введите текст:"))
print(b)

# 2 задание

time=int(input("Введите время в секундах:"))
hours=time//3600
minutes=(time-hours*3600)//60
seconds=(hours*3600+minutes*60)
print(f"Время в формате чч:мм:сс {hours} : {minutes} : {seconds}")

# 3 задание

n= int(input("Введите число"))
summa= (n+int(str(n) + str(n))+ int(str(n)+str(n)+str(n)))
print("сумма чисел n+nn+nnn=", summa)

# 4 задание

a=int(input("Введите целое положительное число"))
max=a % 10
while a>=1:
    a=a//10
    if a % 10 > max:
        max=a % 10
    if a > 9:
        continue
    else:
        print("Самая большая цифра в числе", max)
        break

# 5 задание

viruchka = float(input("Введите выручку"))
izderzki = float(input("Введите издержки"))
if viruchka > izderzki:
    print("Фирма работает с прибылью")
else:
    print("Фирма работает в убыток")


# 6 задание

if viruchka > izderzki:
    print("Рентабельность выручки=", viruchka/izderzki)
    personals=int(input("Введите численность сотрудников фирмы"))
    print(f"прибыль в расчёте на одного сотрудника= {viruchka/personals:.2f}")

# 7 задание

a=int(input("Введите результат пробежки первого дня"))
b=int(input("Введите желаемый результат"))
rezult_days=1
rezult_km=a
while rezult_km<b:
    a=a+0.1
    rezult_days+=1
    rezult_km = rezult_km+a
print(f"спортсмен достигнет результата на %.d день" % rezult_days)



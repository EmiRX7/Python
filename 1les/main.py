# 1 Сумма трех
# Посчитайте сумму трех введенных целых чисел
# 2 Площадь
# Пользователь вводит стороны прямоугольника, выведите его площадь
# 3 Одинаковая четность
# Даны два целых числа: A, B. Проверить истинность высказывания:
#  "Числа A и B имеют одинаковую четность".
# 4 Одно положительное
# Даны три целых числа: A, B, C. Проверить истинность высказывания:
#  "Хотя бы одно из чисел A, B, C положительное".
# 5 Меньшее из двух
# Пользователь вводит два целых числа. Выведите меньшее из них.
# 6 Четырехзначное?
# Пользователь вводит целое число. Выведите YES, если это
#  число является четырехзначным, и NO в противном случае.



1
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)


2
a = float(input())
b = float(input())
c = a * b
print(c)


3
a = int(input())
b = int(input())
c = a%2
d = b%2
if c == d:
    print("Числа A ")
else:

4
a = int(input())
b = int(input())
c = int(input())
if a > 0:
    print("Есть положительные числа ")
elif b > 0:
    print("Есть положительные числа ")
elif c > 0:
    print("Есть положительные числа ")
else:
    print("Нет положительных чисел ")


5
a = int(input())
b = int(input())
if a > b:
    print(b, "меньше")
else:
    print(a, "меньше")


6.1
str = input('number: ')
 
try:
  int(str)
  if len(str) == 4:
    print('YES')
  else:
    print('NO')
except:
  print('ERR')

6.2
a = float(input())
count = 0
while a > 0:
    a = a // 10
    count = count + 1
print(count)


7.1
m = float(input())
n = float(input())
print((m + n - 1) // n)
7.2
import math
m = float(input())
n = float(input())
d = m / n
print(math.ceil(d))


8
a = int(input())
b = int(input())
c = int(input())
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)


9
i = int(input())
j = int(input())
if i == j:
    print("Error")
else:
    print(i + j - 1)



a = int(input())
if (a % 4 == 0) and (a % 100 != 0):
    print("Yes")
else:
    print("No")
# Вводятся числа, пока не введут 0. Найти сумму четных чисел

# a = [1, 2, 3, 4, -5]
# ind = 0
# while x := input() != 0:
#     if a[ind] < 0:
#         print('YES')
#         break
#     ind += 1
# else:
#     print('No')

# Значение переменной-итератера используется
# for i in range(1, 11):
#     print(i ** 2)


# Значение переменной-итератера не используется
# for _ in range(100, 110, 2):  # 0, 1, 2, 3, 4
#     print('HELLO')

# some_list = [-3, 4, 5, 0, 1]
# for a in some_list:
#     print(a)
#
# for ind in range(0, len(some_list)):  # 0, 1, 2, 3, 4
#     print(some_list[ind])


# a = []
# a.append(10)
# print(a)
# 
# 
# a = []
# print(a)
# a[1] = 200
# a[2] = 300
# print(a)


# 9. По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# 11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# 13. 1. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.


# 9 

# num = int(input())
# result = 1

# while num > 1:
#     result *= num
#     num -= 1
# print(result)

# 11

# num = int(input("Введите натуральное число > 1 "))
# i = 0
# chis1 = 0
# chis2 = 1
# while i < num - 2:
#     sum = chis1 + chis2
#     chis1 = chis2
#     chis2 = sum
#     if num == sum:
#         print(sum)
#         break
#     print(sum)
#     i = i + 1 
# else:
#     print(-1)
# print("Значение этого элемента:", chis2)

# 13

# N = int(input("Введите количество дней: "))
# count = 0
# max = 0
# for _ in range(N):
#     temperature = int(input("Введите температуру:  "))

#     if temperature > 0:
#         count += 1
#     else:
#         if max < count:
#             max = count
#             count = 0
# print(max)


# 15 

# N = int(input("Введите количество арбузов: "))
# max = 0
# min = 30000
# for _ in range(N):
#     mass = int(input("Введите вес арбуза: "))
#     if mass > max:
#         max = mass
#     if mass < min:
#         min = mass
# print(max," ", min)

# 17 Проверка на простое число
# N = int(input("Введите число: "))
# count = 0
# for i in range(1, N + 1):
#     if N % i == 0:
#         count += 1
# if count > 2:
#     print("No")
# else:
#     print("Yes")





# H/W

# 10

# n = int(input("Кол-во монет: "))
# reshka, gerb = int(input("Кол-во решек: ")), int(input("Кол-во орлов: "))
# if reshka < gerb:
#     print(reshka)
# else:
#     print(gerb)

# 12

# S, P = int(input("Сумма чисел: ")), int(input("Произведение чисел: "))
# if S > 2000 and P > 1000000:
#     print("Числа больше 1000 ")
# for i in range(0, 1001):
#     for j in range(0, 1001):
#         if i*j == P and i+j == S:
#             x=i
#             y=j
#             print("Первое число: ",x , "Второе число: ", y)
# else:
#     print("Не верные данные")
    
# 14

# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1
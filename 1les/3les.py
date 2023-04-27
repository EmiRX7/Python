# some_str = 'Hello'


# print(some_str[:])

# print(some_str[1:3])

# print(some_str[::-1])



# some_list = [1, 'fgj', True, [1, 2, 3], {1: 2}, (3, 2)]
# print(some_list[2: 3])

# print(some_list[-1])


# some_list = []
# for _ in range(10):
#     number = int(input())
#     some_list.append(number)
# print(some_list)

# import random
# some_list = []
# for _ in range(10):
#     number = random.randint(1, 10)
#     some_list.append(number)
# print(some_list)


# import random
# import time
# some_list = [random.randint(1, 10000) for i in range(10 ** 7)]
# some_set = set(some_list)

# start = time.perf_counter()
# print(11000 in some_list)
# end = time.perf_counter()
# dur1 = end - start


# start = time.perf_counter()
# print(11000 in some_set)
# end = time.perf_counter()
# dur2 = end - start

# print(dur1 / dur2)


# a = [1, 2, 3, 4, 5, 6, 7]
# d = set(a[:-3])
# print(d)

# 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# 2. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть 
# всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

# 3. Напишите программу для печати всех уникальных значений в словаре.

# 4. Дан массив, состоящий из целых чисел. Напишите программу, которая 
# подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)

some_list = [int(input()) for _ in range(10)]

for i in range(len(some_list)):
    
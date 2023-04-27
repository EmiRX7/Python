

# 1. Symma cifr

# a = int(input())
# c = 0
# while a > 0:
#     b = a % 10
#     c = c + b
#     a = a // 10
# print(c)


# 2. 

# a = int(input())
# b = a // 6
# katy = b * 4
# Ser = b
# print("Катя: ", katy, " Сережа и Петя по ", b)

# 3. Chastliv bilet

# a = int(input('Введите номер билета:'))
# b = a // 1000
# chet1 = 0
# chet2 = 0
# while b > 0:
#     c = b % 10
#     chet1 = chet1 + c
#     b = b // 10
# b = a % 1000
# while b > 0:
#     c = b % 10
#     chet2 = chet2 + c
#     b = b // 10
# if chet1 == chet2:
#     print("Yes")
# else:
#     print("No")
    
# 4. 

n = int(input('В-те 1-ю сторону: '))
m = int(input('В-те 2-ю сторону: '))
k = int(input('В-те кол-во долек: '))
if k%n == 0 or k%m == 0:
    print('Yes')
else: 
    print('No')
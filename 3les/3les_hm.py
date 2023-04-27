import random
# 16 

# dlina = int(input("Введите длину списка: "))
# chislo = int(input("Введите число для поиска: "))
# print("Введите элементы: ")
# list = []
# count = 0
# for _ in range(dlina):
#     num = int(input())
#     if num == chislo:
#         count = count + 1
#     list.append(num)
# print(list)
# print(count)

# 16.2(Random list)
# dlina = int(input("Введите длину списка: "))
# chislo = int(input("Введите число для поиска: "))
# list = []
# count = 0
# for _ in range(dlina):
#     num = random.randint(1, 9)
#     if num == chislo:
#         count = count + 1
#     list.append(num)
# print(list)
# print(count)



# 18

# dlina = int(input("Введите длину списка: "))
# chislo = int(input("Введите число для поиска: "))
# list = []
# result2 = 100
# for _ in range(dlina):
#     num = random.randint(1, 100)
#     list.append(num)
#     result = abs(chislo - num)
#     if result < result2:
#         result2 = result
#         blizko = num
# print(blizko)



# 20 
slovo = list(input("Слово: "))
list = [['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'] , ['д', 'к', 'л', 'м', 'п', 'у'], ['б', 'г', 'ё', 'ь', 'я'], ['й', 'ы'], ['ж', 'з', 'х', 'ц', 'ч'], ['ш', 'э', 'ю'], ['ф', 'щ', 'ъ']]
for _ in range(list):
    
print(slovo)
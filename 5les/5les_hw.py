# 26

# a = int(input("Введите число: "))
# b = int(input("Введите степень: "))

# def vozvedenie_v_stepen(a,b):
#     if b == 0:
#         return 1
#     else:
#         return a * vozvedenie_v_stepen(a, b-1)
# print(vozvedenie_v_stepen(a,b))



# 6 

a = 0
b = 0

stroka = input("Введите текст без пробелов: ")
def schet_bukv(a,b):
    count = 1
    for i in range(len(stroka)):
        b = a
        a = stroka[i]
        if a == b:
            count = count + 1
        else:
            if count == 1:
                print(b)
            else:
                print(b, count)
                count = 1
    print(a)
print(schet_bukv(a,b))
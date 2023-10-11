#//////_1задача_/////

# a = int(input('Введите число 1:  '))
# b = int(input('Введите число 2:  '))
# for i in range(a, b + 1):
#     print(f'Ответ:  {i}')


#//////_2задача_/////

# a = int(input("Число 1:  "))
# b = int(input('Число 2:  '))
# if a < b:
#     for i in range(a, b + 1):
#         print(i)
# else:
#     for i in range(a, b - 1, -1):
#         print(f'Ответ:  {i}')

#/////_3задача_/////

# n = int(input('Колличество чисел:  '))
# num = 0
# for i in range(n):
#     num += int(input('Введите числа:  '))
# print(f'Ответ:  {num}')

#//////_4задача_/////

# factorial = 1
# n = int(input('Введите число:  '))
# for i in range(1, n + 1):
#     factorial *= i
# print(f'Факториал = {factorial}')

#//////_5задача_/////

# n = int(input('Колличество ступенек:  '))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="", sep="")
#     print()

#//////_6задача_/////

# n = int(input('Введите число:  '))
# x = 1
# while x**2 <= n:
#     print(f'Число: {x} Его квадрат: {x ** 2}')
#     x += 1

#//////_7задача_/////

# n = int(input('Введите число:  '))
# p = 2
# k = 1
# while p <= n:
#     p *= 2
#     k += 1
# print(f'2 в степени: {k - 1} =  {p // 2}')

#//////_8задача_/////

# x = int(input('Началное колличество км:  '))
# y = int(input('Конечное колличество км:  '))
# i = 1
# while x < y:
#     x *= 1.1
#     i += 1
# print(f'Колличество дней:  {i}')

#//////_9задача_/////

# len = 0
# while int(input('Введите число:  ')) != 0:
#     len += 1
# print(f'Ответ:  {len}')

#//////_10задача_/////
#
# n = int(input('Число:  '))
# i = 0
# while n != 0:
#     x = int(input('Значение:  '))
#     if x != 0 and n < x:
#         i += 1
#     n = x
# print(f'Ответ:  {i}')

#//////_11задача_/////
#
# m1 = 0 #max-1
# m2 = 0 #max-2
# x = int(input('Введите число:  '))
# while x != 0:
#     if x > m1:
#         m2 = m1
#         m1 = x
#     elif x > m2:
#         m2 = x
#     x = int(input('Введите число:  '))
# print(f'Ответ:  {m2}')

#//////_12задача_/////

# n = int(input('Введите число:  '))
# if n == 0:
#     print(0)
# else:
#     a = 0
#     b = 1
#     for i in range(2, n + 1):
#         sum_ab = a + b
#         a = b
#         b = sum_ab
#     print(f'Число Фибоначчи:  {b}')

#//////_12-2задача_/////

# n = int(input('Введите число:  '))
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return (fib(n-1) + fib(n-2))
# print(f'Число Фибоначчи:  {fib(n)}')

#//////_13задача_/////

# n = -1
# len1 = 0
# len2 = 0
# element = int(input('Введите значение:  '))
# while element != 0:
#     if n == element:
#         len1 += 1
#     else:
#         n = element
#         len2 = max(len2, len1)
#         len1 = 1
#     element = int(input('Введите значение 2:  '))
# len2 = max(len2, len1)
# print(f'Количество повторений:  {len2}')

#//////_14задача_/////

# n = input().split()
# for i in range(0, len(n), 2):
#     print(n[i])

#//////_15задача_/////

# n = input().split()
# for i in range(1, len(n)):
#     if n[i] > n[i - 1]:
#         print(n[i])

#//////_16задача_/////
#
# n = [int(i) for i in input().split()]
# x = n[0]
# y = 0
# for i in range(1, len(n)):
#     if (n[i] > x):
#         x = n[i]
#         y = i
# print(f'Число: {x}  Индекс: {y}')

#//////_17задача_/////

# n = [int(i) for i in input('Рост одноклассников в порядке убывания:  ').split()]
# n.sort(reverse=True)
# x = int(input('Рост Пети:  '))
# y = 0
# while y < len(n) and n[y] >= x:
#     y += 1
# print(f'Место в строю:  {y + 1}')

#//////_18задача_/////
#
# n = [int(i) for i in input().split()]
# for i in range(1, len(n), 2):
#     n[i - 1], n[i] = n[i], n[i - 1]
# print(' '.join([str(i) for i in n]))

#//////_19задача_/////

# n = [int(s) for s in input().split()]
# min = 0
# max = 0
# for i in range(1, len(n)):
#     if n[i] > n[max]:
#         max = i
#     if n[i] < n[min]:
#         min = i
# n[min], n[max] = n[max], n[min]
# print(' '.join([str(i) for i in n]))

#//////_20задача_/////

# n = [int(y) for y in input('Введите числа: ').split()]
# x = int(input('Номер индекса для удаления:  '))
# for i in range(x + 1, len(n)):
#     n[i - 1] = n[i]
# n.pop()
# print(' '.join([str(i) for i in n]))


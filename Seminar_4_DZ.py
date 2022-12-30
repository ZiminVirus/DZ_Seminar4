# Урок 4. Данные, функции и модули в Python. Продолжение
# 1. Вычислить число Пи c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# print("Введите с какой точностью нужно вычислить, Н-р: 0.01 - означает 2 знака после точки")
# num = input()
# for el in num:
#     if '.' in num:
#         numbers = num.split('.')[1]
#         numbers = len(numbers)
# print (numbers)
# with open('text.txt', 'r', encoding='utf-8') as file:
#     pinumbers = float(file.read())
#     pi = round(pinumbers,numbers)
#     print (f"При $d = {num}, Pi = {pi}")

# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
#
# print("Введите натуральное число N")
# num = int(input())
# i = 2
# somelist = []
# numbers = num
# while i <= num:
#     if num % i == 0:
#         somelist.append(i)
#         num //= i
#         i = 2
#     else:
#         i = i + 1
# print(f"Простые множители числа {numbers} -> {somelist}")

# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

print ("Введите несколько чисел, через пробел")
num = set(input().split(" "))

print(f"{num}")


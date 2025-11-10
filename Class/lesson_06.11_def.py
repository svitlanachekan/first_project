#Hard level

# не пишимо в одній функції - прописуємо окремо

# два основних випадки - базововий, коли потрібно зупинитись. Треба перевіряти, чи потрібно нам зупинятися

# def countdown(n):
#     if n == 0:
#         print("Start!")
#     else:
#         print(n)
#     # n -= 1 без цього запису
#     countdown(n - 1)

# countdown(5)

#коли треба працювати:

# def countdown_new(n):
#     if n > 0:
#         print(n)
#     # n -= 1 без цього запису
#         countdown_new(n - 1) # викликає на 1 менше
#     print("Start!")

# countdown_new(5)

#13 Напишіть рекурсивну функцію, яка обчислює суму цілих чисел a і b. З арифметичних операцій використовується тільки додавання одиниці і віднімання одиниці.

# -----------

#14. задача

# 5! = 5 * 4 * 3 * 2 * 1
# 1! = 1 

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

'''
factorial(5): 5 * factorial(4)
factorial(4): 4 * factorial(3)
factorial(3): 3 * factorial(2)
factorial(2): 2 * factorial(1)
factorial(1): 1
'''

#-----------
# zum Beispiel: 

# def sum_numbers(a, b):
#     return a + b

# def sqr(a, b):
#     return sum_numbers(a, b) ** 2

# print(sqr(2, 7))

# вийшло в терміналі 81

# перекресна рекурсія-одну ф-цію викликано в іншій

# -----------
# a = 5, b  = 4
# 5 + 4 
# 5 + 1  + 4 - 1 = 6 + 3
# 7 + 2
# 8 + 1
# 9 + 0

# def add_numbers(a, b):
#     if b == 0: #базовий випадок
#         return a
#     return helper(a + 1, b - 1) #рекурсія: викликала наспупну функцію

# def helper(a, b):
#     if b == 0:
#         return a
#     return add_numbers(a + 1, b - 1)

# print(add_numbers(5, 4))
    
# ------------------


# 7+ 5
# 7 (+1) + 5(-1)

# 7 + (-5)
# 7 (-1) + (-5) (+1) => 6 + (-4)

# b == 0 => 
# b >

# -------------------

# УДАЛИЛОСЬ решение №13

# 14.Дано послідовність цілих чисел, що закінчується числом 0. Напишіть рекурсивну функцію, яка друкує цю послідовність в зворотному порядку. При розв’язуванні цього завдання не можна користуватися списками.

# while True:
#     n = int(input("Enter number: "))
#     if n == 0:
#         break

def print_number():
    n = int(input("Enter number: "))
    if n == 0:
        return
    else:
        print_number()
    print(n)

print_number()




    
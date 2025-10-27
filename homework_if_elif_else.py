# 1	Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем для цього користувача, то виводиться повідомлення Password accepted.. У іншому випадку повідомлення буде Sorry, that is the wrong password..

# password = input("Enter password: ")
# password_of_user = "Open"
# if password == password_of_user:
#     print("Password accepted")
# else:
#     print("Sorry, that is the wrong password")

# 2. Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.

# name1 = input("Enter name1: ")
# name2 = input("Enter name2: ")
# if name1 < name2:
#     print(name1, name2)
# else:
#     print(name2, name1)

# 3	Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. Якщо це число або 1 або 2 або 3, то виводиться повідомлення - назва числа, відповідно, One, Two, Three. В усіх інших випадках виводиться слово Unknown.

# num = int(input("Enter a number: "))
# if num == 1:
#     print ("One")
# elif num == 2:
#     print ("Two")
# elif num == 3:
#     print ("Three")
# else:
#     print ("Unknown")

# 4	Користувач вводить дві різних англійські літери в окремих рядках. Напишіть програму, яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.
    
# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# letter1 = input("Enter a letter1: ").lower()
# letter2 = input("Enter a letter2: ").lower()
# place1 = alphabet.index(letter1)+1
# place2 = alphabet.index(letter2)+1
# if place1 < place2:
#     print("Літера", letter1, "розташована перед літерою", letter2)
# else:
#     print("Літера", letter2, "розташована після літери", letter1)

# 5. Напишіть програму, в якій користувач вводить значення температури, і, якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно вивести повідомлення A cold, isn’t it?. Якщо ж температура становить більше 0 і менше 10 градусів Цельсія повідомлення буде Cool., у інших випадках Nice weather we’re having..

# i = int(input("Enter a temperature: "))
# if i <= 0:
#     print("A cold, isn’t it?")
# elif i > 0 and i < 10:
#     print("Cool.")
# else:
#     # print("Nice weather we’re having..")

# 6	Визначте назву геометричної фігури за введеною кількістю її сторін. Програма повинна підтримувати фігури від 3 до 6 сторін. Якщо введена кількість сторін поза межами цього діапазону, програма повинна відображати відповідне повідомлення

# triangle = 3
# square = 4
# pentagon = 5
# hexagon = 6
# figs = [triangle, square, pentagon, hexagon]
# sides = int(input('Введіть число у діапазоні від 3 до 6: '))
# place1 = figs.index(triangle)+1 
# place2 = figs.index(square)+1
# place3 = figs.index(pentagon)+1
# place4 = figs.index(hexagon)+1
# if sides == 3:
#     print("Перед Вами - трикутник")
# elif sides == 4:
#     print("Перед Вами - квадрат")
# elif sides == 5:
#     print("Перед Вами - п'ятикутник")
# elif sides == 6:
#     print("Перед Вами - шестиикутник")
# else:
#     print("Введено неправильне число")

# 7. Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний, червоний або зелений кольори. Номер 0 має зелений колір, для номерів від 1 до 10, непарні номери - червоні, а парні - чорні. Непарні номери від 11 до 18 - чорні, а парні номери - червоні. Непарні номери від 19 до 28 - червоні, а парні номери - чорні. Непарні номери від 29 до 36 - чорні, а парні номери - червоні. Напишіть програму, яка отримує номер (число від 0 до 36) та показує, чи є номер зеленим, червоним або чорним. Програма повинна враховувати варіант, якщо користувач вводить номер, який знаходиться за межами діапазону від 0 до 36.

# number = int(input("Enter a number from 0 till 36: "))
# if number < 0 or number > 36:
#     print("The number doesn't lie in the range.")
# elif number == 0:
#    print("The number is green.")
# elif 1 <= number <= 10:
#     print("The number is black." if number % 2 != 0 else "The number is red.")
# elif 11 <= number <= 18:
#     print("The number is red." if number % 2 != 0 else "The number is black.")
# elif 19 <= number <= 28:
#     print("The number is black." if number % 2 != 0 else "The number is red.")
# elif 29 <= number <= 36:
#     print("The number is red." if number % 2 != 0 else "The number is black.")

# 8. Дано дві точки: A (x1, y1) і B (x2, y2). Напишіть програму, яка визначає, яка із точок знаходиться далі від початку координат.

# A1x1, A2x1 = 1, 4
# A1y1, A2y1 = 2, 4
# B1x2, B2x2 = 3, 4
# B2y2, B2y2 = 2, 4
# dA1 = ((A1x1 ** 2 + A1y1 ** 2) ** 0.5)
# dA2 = ((A2x1 ** 2 + A2y1 ** 2) ** 0.5)
# dB1 = ((B1x2 ** 2 + B2y2 ** 2) ** 0.5)
# dB2 = ((B2x2 ** 2 + B2y2 ** 2) ** 0.5)
# if dA1 <= dB1:
#     print("B")
# if dA2 == dB2:
#     print("The distance is the same")

# 9. Дано натуральное число. Визначити, чи закінчується число парною цифрою.

# num1 = int(input("Enter a nutural number: "))
# if num1 % 2 == 0:
#     print("Even number? True")
# else:
#     print("Even number? False")

# 10.Вводяться координати (x, y) точки A і радіус кола (r). Визначити, чи належить дана точка колу, якщо його центр знаходиться в початку координат.

# x = int(input("Enter a num1: "))
# y = int(input("Enter a num2: "))
# r = int(input("Enter a num3: "))
# d = ((x ** 2 + y ** 2) ** 0.5)
# if d == r:
#     print("The point belongs to the circle")
# else:
#     print("The point is outside the circle")

# 11. Напишіть програму для знаходження коренів квадратного рівняння a*x2 + b*x + c = 0. Користувач вводить значення коефіцієнтів a, b, c. У вхідних даних наведено три пари вхідних значень коефіцієнтів, а у вихідних даних - відповідні повідомлення про кількість коренів або їх відсутність.
# Вхідні дані:
# 8
# 4
# 2
# 3.6
# 10
# -3
# 2
# 4
# 2

# a = float(input("Enter a num1: ")) # time 2:18 Praxis-Lektion 7
# b = float(input("Enter a num2: "))
# c = float(input("Enter a num3: "))
# # 8 * x ** 2 + 4 * x + 2 = 0
# D = b ** 2 - 4 * a * c
# if D < 0:
#     print("No roots")
# elif D > 0:
#     x1 = (- b + D * 0.5) / 2 * a  
#     x2 = (- b - D * 0.5) / 2 * a
#     print(f"{x1} and {x2}")
# else: D == 0
# print(x)

# 12. Відомі рік і номер місяця народження людини, а також рік і номер місяця сьогоднішнього дня (січень - 1 і т. д.). Визначити вік людини (число повних років). У разі збігу вказаних номерів місяців вважати, що пройшов повний рік.
# Вхідні дані:
# 1998
# 3
# 2018
# 2
# Вихідні дані:
# 19

# year_bith = int(input("Enter a year of birth: "))
# month_bith = int(input("Enter a number of month of birth: "))
# year_now = int(input("Enter a year of nowadays: "))
# month_now = int(input("Enter a number of month of nowadays: "))
# year_age = year_now - year_bith
# month_now = month_now - month_bith
# if int(month_bith) == int(month_now):
#     print(year_age)
# else:
#     print(year_age - 1)

# 13. Дано чотирицифрове число. Замінити усі парні цифри числа на символ * і вивести число.
# Вхідні дані:
# 2358
# 2227
# 1353
# Вихідні дані:
# *35*
# ***7
# 1353


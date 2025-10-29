# print("QWERTYdsd34".lower())
# print("QWERTYdsd34".upper())
# print("QWERTYdsd34".isdigit())

# 1. Напишіть програму, яка приймає від користувача рядок, і відображає цей рядок у верхньому і нижньому регістрах.
# s = input("Enter a string: ")
# print(s.upper(), s.title())

# 2. Скласти програму, яка запитує назву баскетбольної команди і повторює її на екрані зі словами: This is a champion!.
# name = input("What a name of the basketball team? ")
# print(name, "This is a champion!")

# 3. Дано натуральне число. Знайти число, що отримується при прочитанні його цифр справа наліво.

# n = input("Enter natural number mote than 0: ")
# print("Reading numbers from riths to left: ", n[::-1])

# 4. Дано рядок. Змініть регістр символів в цьому рядку так, щоб перша буква кожного слова була великою, а інші літери - малими. (метод s.title())

s = input("Enter a sentence: ")
print(s.title())

#5 Дано рядок. Визначити порядковий номер першої вказаної букви. Якщо такої літери немає, вивести нуль.

# line = input("Enter a word: ")
# letter = input("Enter a letter: ")
# if letter in line:
#     place = line.find(letter)+1
#     print("Serial number: ", place)
# else:
#     print("0")

# 6	У рядку є кілька слів, розділених одним або декількома пропусками. Потрібно прибрати з тексту зайві пропуски: два і більше пропусків поспіль, а також всі пропуски на початку і в кінці рядка. На вхід програмі подається рядок, що складається не більше ніж з 255 символів. Надрукувати новий рядок.

# Вхідні дані:
#    Beyond the green     swelling hills of the     Mittel Land rose mighty slopes of forest    up    to the lofty steeps of the Carpathians    themselves
# Вихідні дані:
# Beyond the green swelling hills of the Mittel Land rose mighty slopes of forest up to the lofty steeps of the Carpathians themselves

# 8	Дано рядок, що складається з n цифр (тобто одноцифрових чисел), між якими стоїть n-1 знаків операцій, кожна з яких може бути або +, або -. Обчисліть значення цього виразу. Програма має надрукувати результат обчислення цього виразу.
# НЕ ДОРОБЛЕНО
# ex = input("Enter ex:\n") # 5-3+1
# n = (len(ex) +1) // 2  # number
# print(int(ex[0]) + (1 if ex[1] == "+" else -1) * int(ex[2]) + (1 if ex[3] == "+" else -1) * int(ex[4]))

# ex[::2]
# ex.replace("-, +")
# 2 variant -> circle

# 3 var
# sum = int(ex[0])
# for i in range (1, len(ex)):
#     if ex[i] == "+":
#         sum += int(ex[i+1])
#     elif ex[i] == "-":
#         sum -= int(ex[i+1])
# print(sum)


#4 var


# my_list = ["1", "2", 4, 7]
# # for el in range (le=n(my_list)) #el-змінна циклу
# #     my_list[el] = str(my_list[el])
# # print(my_list)

# new_list = list(map(int, my_list))
# print(new_list)

# ex = ex.replace("-", "+-")
# parts = ex.split("+")
# sum_ex = sum(map(int, parts))
# print(sum_ex)

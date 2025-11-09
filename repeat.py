# main.py
# print("Hello World!")
# print(34)
# print('12.5')
# print(12.5)
# print('Title "Name title"')

# input_print.py -> without mistakes
# n1 = int(input("Enter number1: "))
# n2 = int(input("Enter number2: "))
# print(n1 + n2)

# Hypotenuse -> without mistakes
# side1 = input("Enter leg1: ")
# side2 = input("Enter leg2: ")
# print("Hypotenuse is ", (int(side1) ** 2 + int(side2) ** 2) * 1/2)

# Twice -> without mistakes
# a1 = int(input("Enter a number: "))
# print(str(a1) * 2)

# Name of user -> without mistakes
# n = input("Enter a name: ")
# print("Привіт,", str(n))


# Goodbye -> without mistakes
# n3 = input("Enter a name: ")
# print("До зустрічі,", str(n3))

#---------------------

# num = int(input("Enter a number: "))
# name_of_number = ""

# if num == 1:
#     name_of_number = "One"

# elif num == 2:
#     name_of_number = "Two"

# elif num == 3:
#     name_of_number = "Three"
    
# else:
#     print("Unknown")
#     # name_of_number = "Unknown"

# print(name_of_number)

# --------------

# text = "Python is fun!"
# print(text[-1])

# ----------

# text = "   Beyond the green     swelling hills of the "
# clean = text.strip()
# print(clean)

# ------------------

#8 GMT20251023-070029 Video
# 	
# Дано рядок, що складається з n цифр (тобто одноцифрових чисел), між якими стоїть n-1 знаків операцій, кожна з яких може бути або +, або -. Обчисліть значення цього виразу. Програма має надрукувати результат обчислення цього виразу.

# Вхідні дані:
# 5-3+1
# 6+3-2

# Вихідні дані:
# 3
# 7

# ВИХІДНІ ДАНІ ДЛЯ ВСІХ ВАРІАНТІВ

# task = input("Enter task:\n") # вводиться задача 5-3+1
# len_task = len(task) # виведеться довжина символів (кількість) в задачі

# n = len(task) + 1 // 2 # скільки цифр всього це довжина символів + 1 та поділита на 2, тому що одна з умови задачі цифра це n, а n-1 це кількість операцій (- та +)

# НЕ ЗНАДОБИЛОСЬ task[::2] # отримуємо лише числа (5, 3, 1) - проходимо з початку це start : (цифру не ставимо), stop : це проходдимо до кінця (цифру не сатвимо), step 2 тому що кожний наступний елемент через один, тобто кожний другий, тобто парні значення

#8.1 VARIANT, стільки елементів, скільки ми скажемо

# print(int(task[0]) + (1 if task[1] == "+" else -1) * int(task[2]) +  (1 if task[3] == "+" else -1) * int(task[4])) # візьми число рядка - перший елемент (5), якій відповідає нулоьвому індекcу - [0], зроби з нього число - int та додати умову: сприйми 1 (одиницю) як позитивну через if, в іншому випадку через else відображай її як відʼємну. Визначили для того, щоб був знак, тому що розділяти рядок можна тілько по одному знаку, може мати тільки один роздільник. => 5+(-1)*3+1*1

# ДРУК
# Enter task: 
# 5-3+1
# 3

#8.2 VARIANT у вигляді циклу, порахується в сумі

# sum = 0 #створюється змінна, яка на початку дорівнює нулю, до якого будемо додавати кожне число, але потім взяли 5, щоб потім додавати або віднімати
# sum = 5 # взяли 5 у вигляді int(task[0])
# sum = int(task[0])
# for i in range (1, len(task), 2): # проходжусь по довжині, два цикли, тому що два матиматичних знака
#     sum += (1 if task[i] == "+" else -1) * int(task[i+1])  # є якась сума, яку потрібно вивести в кінець; є і, яка зчитує кожний індекс до непарного індексу; перевіряємо, що це за симовл, а потім додаємо його

# print(sum) # вивели з циклу, щоб не повторювався

# ДРУК
# Enter task:
# 5-3+1
# 3

# 8.3 VARIANT

# sum = int(task[0])
# for i in task:
#     if i == "+":
#         sum += int(task[i+1])
#     elif i == "-":
#         sum -= int(task[i+1])
# print(sum)


# => ДРУК помилка:
# raceback (most recent call last):
#   File "/Users/svitlanachekan/Desktop/DTA/first_project/repeat.py", line 114, in <module>
#     sum -= int(task[i+1])
#                     ~^~
# TypeError: can only concatenate str (not "int") to str

# Тому випрвляємо: проходимося не по всім елемента, а довжині рядка

# sum = int(task[0])
# for i in range(1, len(task)):
#     if task[i] == "+": #i - це індекс, тому звертаюся до рядка
#         sum += int(task[i+1])
#     elif task[i] == "-":
#         sum -= int(task[i+1])
# print(sum)
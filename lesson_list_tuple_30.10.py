# 6. Визначте, скільки різних слів у введеному рядку.

# Вхідні дані:

# a) New Delhi New York Paris Prague Reykjavik
# b) Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend

# Вихідні дані:

# 6
# 19

# text = "New Delhi New York Paris Prague Reykjavik"

# text = text.split()

# new_text = []

# for word in text:
#     if word not in new_text:
#         new_text.append(word)

# print(len(new_text))

# ----------

# Вхідні дані:
# Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend

# text = "Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend"

# text = text.split()

# new_text = []

# for word in text:        
#     if word not in new_text:
#         new_text.append(word)

# print(len(new_text))

# --------

#9 Для введеної послідовності унікальних цілих чисел, поміняйте місцями мінімальний та максимальний елементи цієї послідовності. Надрукуйте отриманий список.

# def set_numbers(numbers):
    
#     min_value = min(numbers)
#     min_index = numbers.index(min_value)
    
#     max_index = numbers.index(max(numbers))

#     numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    
#     return numbers

#     # numbers.index(min(numbers))
# numbers = "1 2 3 6 8 87"
# numbers = list(map(int, numbers.split()))

# print(numbers)
# print(set_numbers(numbers))

# ---------

# 10. Напишіть програму, яка приймає послідовність рядків (порожній рядок для завершення програми) як вхідний рядок і друкує рядки у верхньому регістрі.

# Вхідні дані:

# python
# ruby
# go


# Вихідні дані:

# PYTHON
# RUBY
# GO



# #1 variant 
# while True:
#     line = input("Enter text: ")
#     if line == "":
#         break

#2 variant
# while input() != "":     #НЕ ПРОШЛО
#     print(1)

# №3 variant
# a = "1"
# # while a != "":         # #НЕ ПРОШЛО
#     print
# _______---__________

# lines = []

# while True:
#     line = input("Enter text: ")
#     if line == "":
#         break
#     lines.append(line.upper())

# print(lines)

# for el in lines:
#     print(el)

#------------

#11. У введеному списку цілих чисел, знайдіть і надрукуйте сусідні елементи, які мають однаковий знак. Якщо такої пари немає, не повинно нічого виводитися.



# Вхідні дані:

# 1 -2 -3 5 6 -3 7 8
# Вихідні дані:

# -2 -3
# 5 6
# 7 8

#-----------

# Hard level
#11.У рядку через кому перераховані слова. Сформувати з цих слів новий рядок. Слова мають бути відсортовані за спаданням (від Z до A) без урахування регістру і записані через пропуск.

# text = "horse, cat, parrot, goldfish, dog"
# text_new = text.split(", ")
# text_new.sort(reverse=True)

# print(" ".join(text_new))


# Вхідні дані:

# horse, cat, parrot, goldfish, dog
# Вихідні дані:

# parrot horse goldfish dog cat

#---------
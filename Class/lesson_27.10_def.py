# DEF


# 1.Напишіть функцію, яка отримує ім’я і друкує вітальне повідомлення Hello, <name>.

# def name():
#     print("Hello, name")

# name()

# def name(name):
#     print(f"Hello, {name}")

# name("Oksana")

# name = "Oksana"
# def name_hello(name="NON"):
#     print(f"Hello, {name}")

# name_hello
# name_hello(name)


# name = "Oksana"
# def name_hello(name="NON"):
#     return f"Hello, {name}"

# print(name_hello())
# print(name_hello(name))

# ----------

#2. Напишіть функцію, яка отримує рядок і ціле число n та повертає n копій заданого рядка.

# def copy_string(text, n):
#     return (" " + text + " ") * n 

# text = input("Enter text: ")
# n = int(input("Enter n: "))

# print(copy_string(text, n), end=" ")

# --------

#3.  Напишіть функцію для обчислення суми двох цілих чисел.

# def sum_a_b(a, b):
#     return  a + b

# num_1 = int(input("Num_1: ")) #числа, без 
# num_2 = int(input("Num_2: "))

# print(sum_a_b(num_1, num_2))

# ----------------

# 4. Напишіть функцію для отримання рядка з перших n символів іншого рядка. Якщо довжина рядка менше n, поверніть початковий рядок.

# def n_letter(word, n):
#      if len(word) < n:
#         return word
#      else: 
#         return word[:n]
     
# string = "letter"
# n = 3
# print(n_letter("letter", 3))

# def n_letter(word, n):
#     if len(word) < n:
#         return word
#     return word[:n]
#     print(1) # проверка формулы

# print(n_letter("letter", 3))

# ------------------


# num1 = int(input("Enter a number1: "))
# num2 = int(input("Enter a number2: "))
# num3 = int(input("Enter a number3: "))
# print(f"Cереднє арифметичне трьох чисел {num1}, {num2} та {num3} дорівнює", int((num1 + num2 + num3) // 3))

# age = int(input("Скільки тобі років? "))
# is_adult = age >= 18
# print("Повнолітній?", is_adult)

# number = int(input("Введи число: "))
# print("Парне?", number % 2 == 0)

# x, y = 10, 20
# x > 5 and y < 30
# print(x > 5 and y < 30)
# print(x < 0 or y == 20)
# print(not(x > y))

# date_of__birth = input("Enter a year of birth: ")
# age = 2025 - int(date_of__birth)
# print(f"Твій вік: {age} років")

# n1 = float(input("Enter n1: "))
# n2 = float(input("Enter n2: "))
# op = input("Enter op: (+, - , *, /) ")
# if op == "+":
#    result = n1 + n2
# if op == "-":
#     result = n1 - n2
# if op == "*":
#     result = n1 * n2
# if op == "/":
#     result = n1 / n2
# print(result)

# weight = float(input("Введи вагу (кг): "))
# height = float(input("Введи зріст (м): "))
# bmi = weight / (height ** 2)
# print(f"Твій індекс маси тіла:", bmi)

# sentence = "learning python is easy and fun"
# # print(sentence.capitalize())
# # print(sentence.count("a"))
# print(sentence.find("fun"))

# year_now = int(input("Enter a current year: "))
# date_birth = int(input("Enter your date of birth: "))
# age_now = year_now - date_birth
# age_in_5 = age_now + 5
# print("Через 5 років Вам буде", age_in_5, "років") 

# temperature_c = 25
# temperature_f = temperature_c * 9/5 + 32
# print(f"Температура у Фаренгейтах становить {temperature_f}")

# i = int(input("Enter a temperature: "))
# if i <= 0:
#     print("A cold, isn’t it?")
# elif i > 0 and i < 10:
#     print("Cool.")
# else:
#     print("Nice weather we’re having..")

student = {"name": "Ira", "age": 14}
print(student.get("grade", "Немає даних"))
# String 

#6.	У рядку є кілька слів, розділених одним або декількома пропусками. Потрібно прибрати з тексту зайві пропуски: два і більше пропусків поспіль, а також всі пропуски на початку і в кінці рядка. На вхід програмі подається рядок, що складається не більше ніж з 255 символів. Надрукувати новий рядок.

# Вхідні дані:

#    Beyond the green     swelling hills of the     Mittel Land rose mighty slopes of forest    up    to the lofty steeps of the Carpathians    themselves

# Вихідні дані:

# Beyond the green swelling hills of the Mittel Land rose mighty slopes of forest up to the lofty steeps of the Carpathians themselves

# text = "   Beyond the green     swelling hills of the     Mittel Land rose mighty slopes of forest    up    to the lofty steeps of the Carpathians    themselves"

# text1 = text.split()
# text2 = " ".join(text1)

# print(text2)

# ---------

#8	Дано рядок, що складається з n цифр (тобто одноцифрових чисел), між якими стоїть n-1 знаків операцій, кожна з яких може бути або +, або -. Обчисліть значення цього виразу. Програма має надрукувати результат обчислення цього виразу.

# Вхідні дані:
# 5-3+1
# 6+3-2

# Вихідні дані:
# 3
# 7

# 08.11. ВСПОМНИТЬ ХОТЬ ОДИН ВАРИАНТ ПОСЛЕ ПОВТОРА ЗАВТРА 09.11

# 8.2 Variant

# task = input("Enter a task: ") 
# sum = int(task[0]) # беремо перший символ у рядку, якій дорівнює 5

# for i in range(1, len(task), 2): # перебираємо математичні знаки + та -, які стоять на і-му місці
#     sum += (1 if task [i] == "+" else -1) * int(task[i+1])

# print(sum)

# На виході: 
# Enter a task: 6+3-2
# 7

# 09.11. Смешалось два варианта 2 и 3, исправила, перенос на след строчку забыла \n 
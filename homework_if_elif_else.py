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




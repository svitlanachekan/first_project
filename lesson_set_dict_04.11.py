#6. Напишіть програму для створення словника із введеного рядка символів для підрахунку кількості символів. 

### На виході має бути літера та кількість таких літер у реченні  

# text = "Lorem ipsum dolor sit amet"
# text = list(text) # перетворили на список

# letters = {i: text.count(i) for i in text} # звернулись до словника, переберає кожну літеру

# print(letters)

def task6():
    # для чата GPT
    # 1. Створюємо змінну text і присвоюємо їй рядок
    text = "Lorem ipsum dolor sit amet"

    # 2. Перетворюємо рядок на список символів
    #    Тепер кожна літера, пробіл або знак пунктуації стане окремим елементом списку
    text = list(text)

    # 3. Створюємо словник letters за допомогою dictionary comprehension
    #    - ключі (i) беруться з кожного елемента списку text
    #    - значення (text.count(i)) — це кількість входжень символу i у списку text
    letters = {i: text.count(i) for i in text}

    # 4. Виводимо словник у консоль
    print(letters)


# Вхідні дані:

# Lorem ipsum dolor sit amet
# Вихідні дані:

# {'L': 1, 'o': 3, 'r': 2, 'e': 2, 'm': 3, ' ': 4, 'i': 2, 'p': 1, 's': 2, 'u': 1, 'd': 1, 'l': 1, 't': 2, 'a': 1}

# ---------------

#7.Напишіть програму, яка приймає рядок символів, і обчислює кількість букв і цифр.

def task7():
    text = "Project Gutenberg offers over 59,000 free eBooks"

    number_count = 0
    alpha_count = 0

    for ch in text:
        if ch.isdigit(): 
            number_count += 1 
        elif ch.isalpha():
            alpha_count +=1   
        
    result = {
        "LETTERS": alpha_count,
        "DIGIT": number_count
    }    

    # print(result)

    for key, value in result.items():
        print(key, value)

# 
# Вхідні дані:

# Project Gutenberg offers over 59,000 free eBooks
# Вихідні дані:

# LETTERS 36
# DIGITS 5

#8.Напишіть програму для видалення дублікатів зі списку цілих чисел.

#9. Дано список словників. Кожен словники має 2 пари елементів: ключ 'name' і значення імені студента, ключ 'points' і значення - список балів з різних дисциплін (цілі двоцифрові числа). Надрукуйте найменші значення балів, отримані кожним студентом, в один рядок з пропуском.

# типова на словник, образувати на словник 

#-----------------------

#10. Дано два списки чисел. Порахуйте, скільки унікальних цифр міститься в обох з них.
def task10():
    numbers1 = [1, 5, 3, 8, 0, 1] #є повторення
    numbers2 = [23, 9, 0, 1, 5]

    result = len(set((numbers1 + numbers2)))
    print(result)

# ---------------
# numbers1 = {1, 5, 3, 8, 0, 1} #є повторення
# numbers2 = {23, 9, 0, 1, 5}

# print(numbers1.union(numbers2))
# print(numbers1 | numbers2)  #обʼєднання множин # a | b

# # A - B = A (without B)
# print(numbers1.difference(numbers2)) # a - b
# print(numbers1 - numbers2)

# # обʼєднанні множини мінус перетин
# # {1, 5, 3, 8, 0, 1} ^ {23, 9, 0, 1, 5} = {3, 23, 8, 9} 
# print(numbers1.difference(numbers2)) # a - b
# print(numbers1 - numbers2)

# # перетин множин (спільні елементи)
# # {1, 5, 3, 8, 0, 1} перетин {23, 9, 0, 1, 5} = {3, 23, 8, 9} 
# print(numbers1.difference(numbers2)) # a - b
# print(numbers1 - numbers2)


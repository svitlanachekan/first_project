# Tasks for lesson on the topic of "set() | dict()"
# new_set = set()
# new_set2 = {1, 5, 2}
# new_dict = {}
# new_dict2 = {"key": "value", "key2": "value2"}
# Beginner level

#1.  Створіть словник зі списками добрих справ на сьогодні і на завтра. Надрукуйте із словника добрі справи, які плануєш зробити сьогодні і взавтра.

def task(): #окремо записали завдання і потім записали до функції
    to_do = {
        "today": ["read", "clear", "dog"],
        "tomorrow": ["read", "clear", "call my mom"]
    }

    # print(to_do) не підходить
    print("To do for today")

    for item in to_do["today"]: #звернулась до ключа, тобто повертає значення
        print("-", item)

    print("To do for tomorrow")

    for item in to_do["tomorrow"]: #звернулась до ключа, тобто повертає значення
        print("-", item)

# task()

#-----------


#2. Припустимо, що у нас є словник, в якому ключі є ідентифікаторами, а значення – іменами користувачів. Напишіть програму, яка виводить вітальне повідомлення користувачу на основі його ідентифікатора. Якщо ідентифікатор відсутній у словнику, виводиться вітання для усіх користувачів.

def task2():
    users = { 
        0: "Alice", #одному значенню відповідає однє значання
        1: "Bob",
        2: "Jack"
    }

    user_id = int(input("Your id: "))

    if user_id in users:
        print(f"Hello, {users[user_id]}")
    else:
        print("Hello everybody!")

# Вхідні дані:

# 232
# 550
# 190
# 500
# Вихідні дані:

# Hi, Alice!
# Hi, Bob!
# Hi, Jack!
# Hi, to all!

#-----------

#3. Напишіть програму для сортування за зростанням (за алфавітом) словника за ключами. Словник зберігає пари ключ-значення у вигляді «назва фільму: рік релізу». Інформація виводиться як у вихідних даних: сортування має бути проведено за назвами фільмів.

def task3():
    films = {
        'Avengers: Endgame': 2019, 'Guardians of the Galaxy': 2014, 'Thor': 2011, 'Iron Man': 2008
    }

    sorted_films = dict(sorted(films.items()))

    # print(films) 
    # print()

    # items => до ключа і  до значення
   
    for name, year in sorted_films.items():
        print(f"('{name}, {year})")

# Вихідні дані:

# ('Avengers: Endgame', 2019) ('Guardians of the Galaxy', 2014) ('Iron Man', 2008) ('Thor', 2011) КОРТЕЖ

#-------------

#4.Надрукуйте елементи словника, де ключі - це числа від '1' до 'n' (обидва числа включно), а значення - квадрати ключів. 'n' – ціле число, яке вводить користувач.

# якщо ми звертаємося до ключа , якого немає, проту якщо додати дорівнює (=) то він доповнює елемент з новим ключемю. Якщо ключа був, то він перезаписався

def task4():
    n = int(input("n: ")) #n - змінна

    squares = {} #порожний словник = dict() 

    for i in range(1, n+1):
        #dict[key] = value
        squares[i] = i ** 2 #i-це ключ
    print(squares)

#------------
#2й варіант
def task4():
    n = int(input("n: ")) #n - змінна
    
    squares = {i: i ** 2 for i in range(1, n+1)} #наповне мені ру, число його квадрат => генерується словник
    print(squares)

#--------------

#5.Створіть словник, в кому ключі – назви днів тижня, а значення - цілі числа, що позначають порядковий номер дня тижня від 0 до 6. Надрукуйте назву дня за введеним порядковим номером дня. Якщо введений номер виходить за межі, програма жодних повідомлень не друкує і не повідомляє про помилку.

weeks = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ] #наповнюємо вручну
days = [i for i in range(7)]

# week_dict = {} # в мене є порожній словник, нумерація однакова
# for day in range(7):
#     week_dict[weeks[day]] = days[day]
# print(week_dict)

#zip(key, values)
#zip(список_ключів, список_значень) списки ключів та значень повинні співпадати за розміром
week_dict = {weeks[day]: days[day] for day in range(7)}

week_dict = dict(zip(week, day))



print(week_dict)

# n = номер дня
# for day, number in week_dict.items():
    # if number == n:
    # print(day)
    # break
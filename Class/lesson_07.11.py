#11. На стадіоні є три категорії місць для сидіння: місця класу A коштують a грошових одиниць, місця класу B коштують b грошових одиниць, а місця класу C - c грошових одиниць. Напишіть першу функцію, яка запитує скільки продано квитків на кожний клас місць, і другу функцію, яка відображає суму отриманого доходу від продажу квитків на кожен клас окремо і загалом. Формати введення і виведення такі, як у вхідних і вихідних даних.

# Вхідні дані:

# A
# 20.50
# 45
# B
# 15.75
# 30
# C
# 10.55
# 15
# Вихідні дані:

# ({'A': 922.5, 'B': 472.5, 'C': 158.25}, 1553.25)

#Ввід данних в стовпчик

def get_ticket_data(): # отримуємо дані
    tickets = {} #є словник
    # for _ in range(3): # _ - симовл, я кій можна використовувати замість змінної циклу (наприклад "і"): коли цикл лише для повторень: без підстановки змінна циклу не використовується, тількі на кількість повторень
    #     pass

    '''
    for i in range(3):
        print(1)

    аналог (і - не використовувалося у циклі)

    for _ in range(3):
        print(1)
    '''

    for _ in range(3):
        category = input("category:").strip() #strip прибирає пробіли і обрізає по краю # "    "
        price = float(input("price: ").strip())
        sold = int(input("sold: ").strip())
        tickets[category] = (price, sold) # tuple пишемо кортеж, тому що ціна не змінюється, єдиний спосіб його зміни = його перезаписати
    return tickets

# print(get_ticket_data()) НА ВІХОДЕ #{'a': (2.0, 4), 'c': (4.0, 3), 'f': (3.4, 5)}

# def calculate_revenue(tickets):
#     tickets_by_class = {} #передаю собі словник , можу перезаписати
#     total = 0 #змінна , яка буде разувати фінал

#     #{'a': (3.0, 5)}.items() => ('a', (3.0, 5))
#     # key, value = ()'a': (3.0, 5)
#     # key = 'a', value = (3.0, 5)
#     # category,  НЕ ДОПИСАНО
#     # ccategory, (price, sold) = ('a': (3.0, 5))
#     # category = 'a',  price = 3.0, sold = 5
    
#     for category, (price, sold) in tickets.items(): #пройтись по кожній парі-ключ:значення. Тут є три значення
#         revenue = price * sold
#         tickets_by_class[category] = revenue #це словник
#         total += revenue #total = total + revenue

#     return tickets_by_class, total

# print(calculate_revenue(get_ticket_data()))

# data = get_ticket_data
# result = calculate_revenue
# print(result)


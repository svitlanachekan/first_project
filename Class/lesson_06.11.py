#12. Створіть словник, який відображає ідентифікатори акцій на біржі. Ключами словника є ідентифікатори акцій, а значеннями - дійсні числа - ціни акцій. Надрукуйте ціни акцій та ідентифікатори у порядку зростання ціни.

# Вихідні даніЖ 

# 10.75 FB
# 37.2 HPQ
# 45.23 ACME
# 205.55 IBM
# 612.78 AAPL

stocks = {
    "IBM": 205.55,
    "FB": 10.75,
    "ACME": 45.23,
    "AAPL": 612.78,
    "HPQ": 37.2
    }

# print(stocks.values())
# print(sorted(list(stocks.values())))
# for v in stocks.values():
#     print(v)


def get_value(item):
    return item[1]# витягуеться тільки значення

print(stocks.items())


print(sorted(stocks.items(), key=list(stocks.values())))


# for key, value in stocks.items(): #проходжусь по заданому словнику, створюється дві змінни (іья акції та занчення акції)
# #   print(key, value)
#     print(value, key)
# # щоб отримати список значень, 

# --------------------

#14. Напишіть програму, яка зможе підрахувати слова у введеному рядку, розділені пропуском і вивести отриману статистику: для кожного унікального слова обчислити число його повторень (без урахування регістру), слова не повинні повторюватися, порядок слів довільний.

# Вхідні дані:

# a bb acD bb abc ac BCD a
# Вихідні дані:

# a 2
# bb 2
# acd 1
# abc 1
# ac 1
# bcd 1

text = "a bb acD bb abc ac BCD a".lower().split()
result = {}
for word in text:
    # result[word] = text.count(word)
    result[word] = result.get(word, 0) + 1

for key, value in result.items():
    print(key, value)
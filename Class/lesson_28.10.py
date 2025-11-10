# Middle level

# 10.Напишіть функцію, яка отримує значення середньомісячної кількості опадів по місяцях (в мм) і повертає загальний обсяг опадів протягом року, середньорічну кількість опадів, назви місяців та значення з найвищим та найменшим числом опадів протягом року.

# Вхідні дані:

# 22 22 24 49 72 98 101 82 51 40 36 24
# Вихідні дані:

# (621.0, 51.75, (101.0, 'July'), (22.0, 'January'))

# def rainfall_statistics(values):
#     months = [
#         "Jan", "Feb", "March",
#         "April", "May", "June", 
#         "July", "Aug", "Sep", 
#         "Oct", "Nov", "Dec"
#         ]
#     rain = list(map(float, values.split()))

#     total = sum(rain)

#     average = total / 12 #len(rain) = 12

#     max_rain = max(rain)
#     min_rain = min(rain)

#     max_month = months[rain.index(max_rain)] 
#     min_month = months[rain.index(min_rain)]

#     return (total, average, (max_rain, max_month),(min_rain, min_month))

# date = "22 22 24 49 72 98 101 82 51 40 36 24"

# result = rainfall_statistics(date)

# print(result)
#-------

def rainfall_statistics(values):
    months = [
        "Jan", "Feb", "March",
        "April", "May", "June", 
        "July", "Aug", "Sep", 
        "Oct", "Nov", "Dec"
        ]
    rain = list(map(float, values.split()))

    total = sum(rain)

    average = total / 12 #len(rain) = 12

    max_rain = max(rain)
    min_rain = min(rain)


    # if
    max_month = months[rain.index(max_rain)] 
    min_month = months[rain.index(min_rain)]

    return (total, average, (max_rain, max_month),(min_rain, min_month))

date = "22 22 24 49 72 98 101 82 51 40 36 24"

result = rainfall_statistics(date)

print(result)
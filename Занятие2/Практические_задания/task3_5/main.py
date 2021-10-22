wind = int(input())

# TODO напишите с помощью if-elif-else условие проверки скорости ветра
if 1 <= wind <= 4:
    print("слабый")
elif 5 <= wind <= 10:
    ...
elif 11 <= wind <= 18:
    pass
#else:
   # print("ураганный")   # если введём -10 то тоже сюда упадёт в else (если не пропишем услованеи)
elif wind > 19:
    print("ураганный")
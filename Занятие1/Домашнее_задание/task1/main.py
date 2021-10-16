speed = input("Скорость передачи (байт/с): ") # Напишите ваше решение
time = input("Время закачки составило(мин): ")
size = round(int(speed) * int(time) * 60 * 9.31 ** -10,3)
print(str(size) + " размер файла в Гб")

coast = input('рублей за Гбайт: ')
price = (size // 10) * int(coast)
print(price)

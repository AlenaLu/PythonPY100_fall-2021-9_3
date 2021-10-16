DAYS_OF_YEAR = 365  # количество дней в году
print("Год рождения?")
start_year = int(input())  # TODO запросить у пользователя год рождения
print("Какой сейчас год?")
current_year = int(input())  # TODO запросить у пользователя текущий год
print(type(current_year))
print((current_year - start_year) * DAYS_OF_YEAR)  # TODO посчитать и распечатать количество прожитых дней

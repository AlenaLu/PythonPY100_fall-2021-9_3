mount = ...  # TODO запросить месяц у пользователя. Номер месяца - целочисленное значение!



# оператор in для проверки вхождения значения в какую либо последовательность
# если значение содерж-ся в посл-ти то нам вернётся True, если нет то вернётся False
if mount in [ 3, 4, 5]:
    print("Весна")
elif mount in [range(6, 9)]:
    print("Лето")
elif mount in (9, 10, 11):
    print("Осень")
elif mount in {12, 1, 2}:
    print("Зима")

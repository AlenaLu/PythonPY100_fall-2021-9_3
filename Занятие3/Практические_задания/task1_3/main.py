def incorrect_func(name_arg=[]):
    # name_arg является локальной переменной
    print("Аргумент до изменения", name_arg)
    name_arg.append(1)
    print("Аргумент после изменения", name_arg)


def incorrect_main():
    # вызовем два раза одну и ту же функцию
    incorrect_func()
    print('-----')  #просто для визуального разделения
    incorrect_func()
# вот так лучше не делать, функция получается нечистая

# установим аргумент name_arg пустым а внутри функции будем проверять его
def correct_func(name_arg=None):
    if name_arg is None:  # id(name_arg) ==id(None)
        name_arg = []  #cоздание списка внутри тела
    print("Аргумент до изменения", name_arg)
    name_arg.append(1)
    print("Аргумент после изменения", name_arg)


def correct_main():
    # вызовем два раза одну и ту же функцию
    correct_func()
    print('-----')
    correct_func()
    print('-----')
    correct_func([123])
    print('-----')
    correct_func(name_arg=[123])


if __name__ == "__main__":
    #incorrect_main()
    correct_main()

def pow_func(base, pow_=2): #возвести какое число в степень
    # base ** pow_ -> реализовать через цикл while
    # #pow_ задаёт кол-во шагов сколько раз нужно перемножить
    # 1*a*a*a...*a

    res = 1
    while pow_ > 0:
        res *= base
        pow_ -= 1

    return res



if __name__ == "__main__":
    a = 5
    n = 3

    print(pow_func(a, n))

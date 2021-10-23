PI = 3.14  #constant


def square_circle(r):  #функция которая будет искать площадь круга
    return PI * r ** 2   #функция ищет r в локальной области видимости


if __name__ == "__main__":
    square = square_circle(5)  #r=5 и подставляется в строку 5
    print(square)

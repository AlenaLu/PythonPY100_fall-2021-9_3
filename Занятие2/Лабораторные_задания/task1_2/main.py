# TODO
A = int(input("Введите число: "))
B = int(input("Введите число: "))

cond1 = A % 2 == 0
cond2 = B % 2 == 0

if not (cond1 or cond2):
    print("оба числа нечётные")
else:
    print()

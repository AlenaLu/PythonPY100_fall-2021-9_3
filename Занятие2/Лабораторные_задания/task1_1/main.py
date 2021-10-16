# TODO
a = input("Введите число: ")
cond1 = int(a) % 2 == 0
cond2 = int(a) % 3 == 0

if cond1 or cond2:
    print("число кратно 2 или 3")
else:
    print("число не кратно 2 или 3")

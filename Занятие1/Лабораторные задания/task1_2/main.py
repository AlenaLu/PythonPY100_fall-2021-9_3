NALOG = 0.13 # ставка процента подоходного налога

print("Размер вашего оклада?")
oklad = int(input())

a = float(oklad * NALOG)
b = float(oklad - a)

print(a,b)
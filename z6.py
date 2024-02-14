import math
R = int(input("Введите число: "))
r = int(input("Введите число: "))
h = int(input("Введите число: "))

V = 1/3 * math.pi * (R**2 + r**2 + R*r) * h
I =  math.sqrt(h**2 +(R - r)**2)
S = math.pi * (R+r)*I + math.pi * R**2 + math.pi * r**2
print("Площадь поверхности равна: " + str(S))
print("объем усеченного конуса равен: : " + str(V))
print("еще что то равно: " + str(I))

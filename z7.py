import math
R = int(input("Введите число: "))
a = int(input("Введите число: "))
b = (math.sqrt(2*R**2- 2*R) * math.sqrt(R**2- (a**2/4)))
print(b)

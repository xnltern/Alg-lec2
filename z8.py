import math
a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
p = (a+b+c)/2
R = (a*b*c) / (4 * (math.sqrt( p*((p-a)*(p-b)*(p-c)))))
r = math.sqrt(((p-a)*(p-b)*(p-c))/p)
print(r)
print(R)

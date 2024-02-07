import math
k = int(input("Введите число: " ))
x = int(input("Введите число: "))
y = int(input("Введите число: "))
res = 100 **3 - 92**2 + k
res_2 = math.sqrt((1 - math.cos(x))/2)
res_3 = (math.sqrt(abs(x)) * math.log(x**2))/ (-5/4*x + math.exp(x/2))
res_4 = (math.sqrt(math.sin(x)**2) + (math.cos(y**3)**2))
print(res)
print(res_2)
print(res_3)
print(res_4)

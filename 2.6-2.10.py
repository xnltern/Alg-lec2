#6
a,b,c = map(int, input("Введите числа").split())
if a < b < c:
    print("равенство выполняется")
else:
    print("неравенство не выполняется")
#7
a, b, c = map(int, input("Введите числа").split())
if a >= b >= c:
    a*=2
    b*=2
    c*=2
    print(a,b,c)
else:
    a = abs(a)
    b = abs(b)
    c = abs(c)
    print(a,b,c)
#8
b, c = map(int, input("Введите числа").split())
if b <= c:
    b = 0
    print(b,c)
else:
    print(b,c)
#9
a, b, c = map(int, input("Введите числа").split())
if a >= 1 and a <= 3:
    print(a)
else:
        print(" ")
if b >= 1 and b <= 3:
    print(b)
else:
        print(" ")
if c >= 1 and c <= 3:
    print(c)
else:
        print(" ")
#10
a, b, c = map(int, input("Введите числа").split())
if b-a == c-b or b+a == c+b:
    print("a,b,c - члены арифметической прогрессии")
    print("разность - " +str(b-a))
else:
    print("a b c - не члены арифметической прогрессии")

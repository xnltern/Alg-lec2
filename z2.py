N = int(input("Введите количество учеников: "))
A = int(input("Введите количество пятерок: "))
B = int(input("Введите количество четверок: "))
C = int(input("Введите количество двоек: "))
X = N - (A + B + C)
X_percent = (X * 100) / N
print("количество троек " + str(X_percent))

a = int(input())
v = 0
if a > 1:
    for i in range(1,a+1):
        if a%i==0:
            v+=1
if v ==2:
    print(f" {a} prost")
else:
    print(f" {a} neprost")

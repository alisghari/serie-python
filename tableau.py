while True:
    n=int(input("taper le nombre de  casse"))
    if n in range (5,20):
        break
T=[0]*n
for i in range (n):
    while True:
        print("T[",i,"]=")
        T[i]=(input())
    if (T % 2) == 0:
         print(i)

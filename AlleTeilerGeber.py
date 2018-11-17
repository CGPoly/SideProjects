# diese Programmierung gibt dir alle Teiler einer beliebigen Zahl:
N = int(input("Ich rechne alle teiler aus!"))
t = 2
for i in range(N):
    if N % t == 0:
        if t == N:
            print()
        elif t == 1:
            print()
        else:
            print(t)
    t = t+1

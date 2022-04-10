N = int(input())
i = a = b = 1
while i < N:
    a, b = b, (a+b)%15746
    i += 1
print(b)
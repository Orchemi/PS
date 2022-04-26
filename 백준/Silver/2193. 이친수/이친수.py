N = int(input())
a = b = 1
i = 2
while i < N:
    a, b = b, a+b
    i += 1
print(b)
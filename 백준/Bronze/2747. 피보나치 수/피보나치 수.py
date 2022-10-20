n = int(input())
i, a, b = 0, 0, 1
while i < n:
    a, b = b, a+b
    i += 1
print(a)
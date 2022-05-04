N = int(input())
a, b = 3, 2
while N > 1:
    c = a
    a += b*2
    b += c
    a = a%9901 if a > 9901 else a
    b = b%9901 if b > 9901 else b
    N -= 1
print(a)
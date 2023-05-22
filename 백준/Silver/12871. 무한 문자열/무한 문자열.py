from math import lcm

a = input()
b = input()
al, bl = len(a), len(b)
K = lcm(al, bl)

a *= K//al
b *= K//bl
print(1 if a==b else 0)
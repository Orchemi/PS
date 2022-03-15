L = int(input())
txt = list(map(ord, input()))
txt = [i-96 for i in txt]

r = 31
M = 1234567891

H = 0
for i, val in enumerate(txt):
    H += val * (r**i)

print(H%M)
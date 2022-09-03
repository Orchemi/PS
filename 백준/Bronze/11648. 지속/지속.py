n = int(input())
cnt = 0
while n > 9:
    g = 1
    for k in str(n):
        g *= int(k)
    n = g
    cnt += 1

print(cnt)
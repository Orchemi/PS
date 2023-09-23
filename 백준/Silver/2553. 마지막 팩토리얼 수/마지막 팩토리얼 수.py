N = int(input())
ret = 1
for n in range(1, N+1):
    ret *= n
    while not ret % 10:
        ret = ret // 10
    ret %= 10000000

print(ret%10)
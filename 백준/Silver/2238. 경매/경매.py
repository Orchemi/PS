import sys
input = sys.stdin.readline

U, N = map(int, input().split())
D = {}
for _ in range(N):
    name, price = input().split()
    price = int(price)

    if not D.get(price, []):
        D[price] = []
    D[price].append(name)

min_cnt = 1e7
min_price = 1e7
for price, arr in D.items():
    cnt = len(arr)
    if min_cnt > cnt:
        min_cnt = cnt
        min_price = price

    elif min_cnt == cnt:
        min_price = min(min_price, price)

print(D[min_price][0], min_price)
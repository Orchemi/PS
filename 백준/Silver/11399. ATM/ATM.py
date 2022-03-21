N = int(input())
arr = sorted(list(map(int, input().split())))
total = 0
ssum = 0
for a in arr:
    ssum += a
    total += ssum

print(total)
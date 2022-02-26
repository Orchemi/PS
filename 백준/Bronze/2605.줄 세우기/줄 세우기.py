N = int(input())
arr = list(map(int, input().split()))

lst = []
i = 1
for a in arr:
    lst.insert(a, i)
    i += 1

print(*reversed(lst))
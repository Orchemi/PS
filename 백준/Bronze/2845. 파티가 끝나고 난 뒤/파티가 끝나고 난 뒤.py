a, b = map(int, input().split())
c = a*b
arr = list(map(int, input().split()))
print(*[n-c for n in arr])
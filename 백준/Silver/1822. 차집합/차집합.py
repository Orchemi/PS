a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
ret = sorted(list(A-B))
print(len(ret))
if ret: print(*ret)
arr = [0]
for _ in range(4):
    a, b = map(int, input().split())
    arr.append(arr[-1]-a+b)
print(max(arr))
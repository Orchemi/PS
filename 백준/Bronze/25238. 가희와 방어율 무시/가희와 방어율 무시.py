a, b = map(int, input().split())
ret = a * (100-b) / 100
print(1 if ret < 100 else 0)
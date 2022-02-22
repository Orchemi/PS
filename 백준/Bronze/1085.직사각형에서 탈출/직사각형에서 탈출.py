x, y, w, h = map(int, input().split())
min_val = min(x, y, h-y, w-x)
print(min_val)
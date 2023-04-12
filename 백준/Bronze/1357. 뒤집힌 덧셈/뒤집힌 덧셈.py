def rev(x):
    return int(str(x)[::-1])

a, b = map(int, input().split())
print(rev(rev(a)+rev(b)))
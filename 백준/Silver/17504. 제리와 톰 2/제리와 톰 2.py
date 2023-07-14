N = int(input())
arr = list(map(int, input().split()))

m, s = arr.pop(), 1
while arr:
    p = arr.pop()
    s += m*p
    s, m = m, s

print(m-s, m)
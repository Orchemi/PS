import sys
input = sys.stdin.readline

Q = []
start = 0
end = 0
size = 0

N = int(input())
for _ in range(N):
    a = input().split()
    if len(a)==2:
        pushN = a[1]
    Fn = a[0]

    if Fn=='push':
        Q.append(pushN)
        end += 1
        size += 1

    elif Fn=='pop':
        if start < end:
            print(Q[start])
            size -= 1
            start += 1
        else:
            print(-1)

    elif Fn=='size':
        print(size)

    elif Fn=='empty':
        print(0 if size else 1)

    elif Fn=='front':
        print(Q[start] if size else -1)

    elif Fn=='back':
        print(Q[end-1] if size else -1)
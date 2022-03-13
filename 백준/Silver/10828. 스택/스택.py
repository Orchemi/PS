import sys
input = sys.stdin.readline

N = int(input())
stack = []
size = 0
for _ in range(N):
    a = input().split()
    if len(a)==2:
        pushN = a[1]
    Fn = a[0]

    if Fn=='push':
        stack.append(pushN)
        size += 1
    elif Fn=='pop':
        if size:
            print(stack.pop())
            size -= 1
        else:
            print(-1)
    elif Fn=='size':
        print(size)
    elif Fn=='top':
        if size:
            print(stack[-1])
        else:
            print(-1)
    elif Fn=='empty':
        print(0 if size else 1)
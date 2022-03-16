import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    a = int(input())
    stack.append(a) if a else stack.pop()

ret = 0
for s in stack:
    ret += s

print(ret)
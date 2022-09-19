import sys
input = sys.stdin.readline

def main():
    txt = list(input().strip())
    stack = []
    while txt:
        c = txt.pop()
        if not stack or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()

    return 0 if stack else 1

N = int(input())
ret = 0
for _ in range(N):
    ret += main()
print(ret)
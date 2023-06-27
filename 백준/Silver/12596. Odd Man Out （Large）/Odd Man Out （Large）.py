import sys
input = sys.stdin.readline

def main():
    N = int(input())
    p = set()
    lst = list(map(int, input().split()))
    for n in lst:
        if n in p:
            p.remove(n)
        else:
            p.add(n)

    return p.pop()

T = int(input())
for t in range(T):
    print(f'Case #{t+1}: {main()}')
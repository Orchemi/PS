import sys
input = sys.stdin.readline

def main():
    def one(L):
        S.append(op[1])
        L += 1
        return L

    def two(L):
        if not L: print(-1)
        else:
            print(S.pop())
            L -= 1
        return L

    def three(L):
        print(L)
        return L

    def four(L):
        print(0 if L else 1)
        return L

    def five(L):
        print(S[-1] if S else -1)
        return L

    funcs = [0, one, two, three, four, five]
    S = []
    L = 0
    N = int(input())
    for _ in range(N):
        op = list(map(int, input().split()))
        n = op[0]
        L = funcs[n](L)

main()
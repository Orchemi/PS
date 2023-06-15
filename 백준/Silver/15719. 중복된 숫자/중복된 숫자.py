import sys
input = sys.stdin.readline

def main():
    N = int(input())
    M = (N*(N-1))//2
    S = 0
    tmp = ''
    line = input()
    for t in line:
        if t==' ':
            S += int(tmp)
            tmp = ''
        else:
            tmp += t

    if tmp: S += int(tmp)
    return S-M

print(main())
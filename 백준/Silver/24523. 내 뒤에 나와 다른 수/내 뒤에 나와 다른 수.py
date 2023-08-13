import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = input().split()
    cur = arr[0]
    cnt = 1
    i = 0
    ret = []
    while True:
        if i+1 == N:
            ret.append((-1, cnt))
            break

        if arr[i+1] == cur:
            cnt += 1
        else:
            ret.append((i+2, cnt))
            cur = arr[i+1]
            cnt = 1
        i += 1

    for i, r in ret:
        print(*[i]*r, end=' ')

main()
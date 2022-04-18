import sys
input = sys.stdin.readline

N = int(input())
L = int(input())
txt = list(map(lambda x: (0 if x=='O' else 1), input()))

k = 0
check = 1
cnt = 0
l = 0
while k < L:
    flag = 0
    # 시작
    if txt[k] == check:
        while k < L and txt[k]==check:
            check ^= 1
            l += 1
            k += 1
            flag = 1

        if l >= 2*N+1:
            cnt += (l-(2*N-1))>>1
        l = 1 if k<L and txt[k] else 0

    k = k if flag else k+1

print(cnt)
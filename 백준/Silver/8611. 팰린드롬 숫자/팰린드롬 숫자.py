import sys
input = sys.stdin.readline
from collections import deque

def main():
    def convert_num(N, n):
        k = 1
        while k <= N:
            k *= n
        k //=  n
        ret = ''
        while k >= 1:
            a, b = N//k, N%k
            ret += str(a)
            N = b
            k //= n

        return ret

    def check_pal(n):
        Q = deque(list(n))
        l = len(Q)
        while l > 1:
            if Q[0] != Q[-1]: return False
            Q.popleft()
            Q.pop()
            l -= 2
        return True

    N = int(input())
    ret = []
    for n in range(2, 11):
        converted_num = convert_num(N, n)
        if check_pal(converted_num):
            ret.append((n, converted_num))
    return ret

ret = main()
if ret:
    for pair in ret:
        print(*pair)

else:
    print('NIE')
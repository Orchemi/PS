def middle():
    M = int(input())
    ret = N-1
    ret += 8*(M//2)

    M %= 2
    pos = N-1
    d = 1
    while True:
        if pos+d==N:
            if not M: return ret
            M = 0
        pos += d
        ret += 1
        if pos==5: d = -1
        elif pos==0: d = 1

def side(start):
    M = int(input())
    return start + 8*M

N = int(input())
print(middle() if 1<N<5 else side(N-1))
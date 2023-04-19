def find_t(n):
    if t[n]: return t[n]

    i = 0
    ret = 0
    while i < n:
        ret += find_t(i)*find_t(n-i-1)
        i+=1
    t[n] = ret
    return t[n]


t = [0]*36
t[0] = 1
N = int(input())
print(find_t(N))
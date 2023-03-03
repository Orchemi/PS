N = int(input())
cnt = 0
n = 1
while n <= int(N**(1/2))+1:
    m = n
    while n*m <= N:
        m += 1
        cnt += 1
    n += 1
print(cnt)
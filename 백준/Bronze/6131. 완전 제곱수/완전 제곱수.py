a = 2
N = int(input())
cnt = 0
while a < N:
    b = 1
    while b < a:
        if (a+b)*(a-b)==N:
            cnt += 1
        b += 1
    a += 1
print(cnt)
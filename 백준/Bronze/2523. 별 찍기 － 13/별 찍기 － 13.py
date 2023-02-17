N = int(input())
n = 1
while n < N:
    print('*'*n)
    n += 1

print('*'*N)

while n > 1:
    n -= 1
    print('*'*n)
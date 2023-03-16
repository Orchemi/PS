N = int(input())
b = N-1
s = 1
while True:
    print(' '*b, end='')
    print('*'*s)
    if not b: break
    b -= 1
    s += 2

b = 1
s -= 2
while True:
    print(' '*b, end='')
    print('*'*s)
    if b==N: break
    b += 1
    s -= 2
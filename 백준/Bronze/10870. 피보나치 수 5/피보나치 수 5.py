N = int(input())

if N < 2:
    print(N)
    quit()

a, b = 0, 1
k = 1
while k < N:
    a, b = b, a+b
    k += 1
print(b)

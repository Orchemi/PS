N = int(input())
N *= 2
M = int(N**(1/2))

while True:
    if M*(M+1) <= N: break
    M -= 1
print(M)
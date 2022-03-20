N = int(input())
fact = [1]*(N+1)
for i in range(2, N+1):
    fact[i] = i*fact[i-1]

a = N
b = 0
ret = 0
while a >= 0:
    ret += fact[a+b]//(fact[a]*fact[b])*(2**b)
    a, b = a-2, b+1
    
print(ret % 10007)
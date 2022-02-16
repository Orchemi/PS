A, B = map(int, input().split())

min_v = 1
i = 2
while (A!=1) and (B!=1) and (i <= max(A,B)):
    if not (A%i)+(B%i):
        min_v *= i
        A, B = A//i, B//i
        continue
    i+=1

print(min_v)
print(A*B*min_v)
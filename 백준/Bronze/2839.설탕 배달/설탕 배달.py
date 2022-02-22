N = int(input())

A, B = N//5, N % 5

if N == 4 or N == 7:
    result = -1
elif B == 0:
    result = A
elif B % 3 == 0:
    result = A + B//3
elif (B+5) % 3 == 0:
    result = (A-1) + (B+5)//3
elif (B+10) % 3 == 0:
    result = (A-2) + (B+10)//3
elif (N % 3) == 0:
    result = N//3
else:
    result = -1

print(result)
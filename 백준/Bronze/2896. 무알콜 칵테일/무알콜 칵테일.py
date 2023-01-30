A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = min([A[i]/B[i] for i in range(3)])
D = [A[i]-B[i]*C for i in range(3)]
print(*D)
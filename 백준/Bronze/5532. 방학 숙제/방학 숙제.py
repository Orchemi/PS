a = [int(input()) for _ in range(5)]
A = a[1]//a[3]+1 if a[1]%a[3] else a[1]//a[3]
B = a[2]//a[4]+1 if a[2]%a[4] else a[2]//a[4]
print(a[0]-max(A,B))
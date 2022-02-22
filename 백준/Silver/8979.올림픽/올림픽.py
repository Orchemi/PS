N, K = map(int, input().split())
dict1 = {}

for n in range(N):
    a = list(map(int, input().split()))
    a_score = a[1]*(10**12) + a[2]*(10**6) + a[3]
    dict1[a[0]] = a_score

c = dict1.get(K)

cnt = 1
for val in dict1.values():
    if val < c:
        cnt += 1

print(cnt)
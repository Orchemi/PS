K = int(input())
cnt = 0
for N in range(0, K+1, 5):
    while not N % 5 and N // 5:
        N = N // 5
        cnt += 1
print(cnt)
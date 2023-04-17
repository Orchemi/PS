N = int(input())
M = int(input())
lights = list(map(int, input().split()))
ret = max(lights[0], N-lights[-1])
for i in range(1, M):
    dis = lights[i]-lights[i-1]
    cur = dis//2+1 if dis%2 else dis//2
    ret = max(ret, cur)
print(ret)
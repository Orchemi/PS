n,k = map(int,input().split())
nation = [list(map(int,input().split())) for _ in range(n)]
nation.sort(key = lambda x : (-x[1],-x[2],-x[3]))

record = (nation[0][1],nation[0][2],nation[0][3])
rank,cnt = 1,0
for num,a,b,c in nation:
    cnt+=1
    if (a,b,c) != record:
        rank = cnt
        record = (a,b,c)
    if num == k:
        print(rank)
        break
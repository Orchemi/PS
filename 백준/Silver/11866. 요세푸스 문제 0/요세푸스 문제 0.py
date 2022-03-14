N, K = map(int, input().split())
size = N
arr = list(range(1, N+1))
visited = [0]*N
ret = []

sch_i = 0
# size가 0 이 아닌동안 실행
while size:
    check = 0
    while True:
        # 있는 원소라면 check 1 추가
        if not visited[sch_i%N]:
            check += 1

        if check==K:
            visited[sch_i%N] = 1
            ret.append(arr[sch_i%N])
            size -= 1
            break

        sch_i += 1

print('<', end='')
print(*ret, sep=', ', end='')
print('>')
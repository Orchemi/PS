T = 1
while True:
    N = int(input())
    if not N: break

    students = [input() for _ in range(N)]
    checked = [2]*N
    for _ in range(2*N-1):
        n, c = input().split()
        n = int(n)-1
        checked[n] -= 1
        
    for i in range(N):
        if checked[i]:
            print(T, students[i])
            break
    T += 1
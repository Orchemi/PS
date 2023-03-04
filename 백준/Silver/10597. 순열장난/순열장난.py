def main():
    def dfs(i, visit):
        if i == l: return True
        n = int(N[i])
        if n>M: return False
        if not visit[n]:
            stack.append(n)
            new_visit = visit[:]
            new_visit[n] = 1
            if dfs(i+1, new_visit): return True
            stack.pop()
        if i==l-1: return False

        n = int(N[i:i+2])
        if n>M: return False

        if not visit[n]:
            stack.append(n)
            new_visit = visit[:]
            new_visit[n] = 1
            if dfs(i+2, new_visit): return True
            stack.pop()
        return False

    N = input()
    l = len(N)
    M = l if l < 10 else 9 + (l-9)//2

    stack = []
    visit = [0]*(M+1)
    visit[0] = 1
    dfs(0, visit[:])
    return stack

print(*main())
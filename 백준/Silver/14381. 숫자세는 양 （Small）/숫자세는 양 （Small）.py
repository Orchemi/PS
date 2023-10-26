def main():
    N = int(input())
    S = {str(n) for n in range(10)}
    for n in range(1, 1000):
        M = N*n
        MS = set(str(M))
        S -= MS
        if not S: return M
    return 'INSOMNIA'

T = int(input())
for t in range(T):
    print(f'Case #{t+1}: {main()}')
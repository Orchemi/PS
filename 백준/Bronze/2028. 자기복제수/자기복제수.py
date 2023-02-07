def main():
    N = int(input())
    M = N**2
    print('YES' if str(M)[-len(str(N)):]==str(N) else 'NO')
for _ in range(int(input())): main()
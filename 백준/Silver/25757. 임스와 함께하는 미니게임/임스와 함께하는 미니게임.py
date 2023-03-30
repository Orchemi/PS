import sys
input = sys.stdin.readline

N, G = input().split()
D = {'Y':1,'F':2,'O':3}
S = len(set(input() for _ in range(int(N))))
print(S//D[G])
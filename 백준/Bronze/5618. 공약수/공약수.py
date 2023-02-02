def find_ys(N):
    ys = set()
    for n in range(1, int(N**(1/2))+1):
        if N%n: continue
        ys.add(n)
        ys.add(N//n)
    return ys

def main():
    T = int(input())
    yss = [find_ys(N) for N in list(map(int, input().split()))]
    S = yss.pop()
    while yss:
        S = S & yss.pop()
    return sorted(list(S))

for n in main():
    print(n)
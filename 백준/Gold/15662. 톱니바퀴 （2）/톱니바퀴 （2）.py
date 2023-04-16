from collections import deque

def main():
    def make_wheels():
        wheels = []
        for _ in range(T):
            wheels.append(deque())
            lst = list(map(int, input()))
            for i in lst:
                wheels[-1].append(i)
        return wheels

    def turn(n, d):
        if n in turned: return
        turned.add(n)

        if n-1>=0 and wheels[n][6]^wheels[n-1][2]:
            turn(n-1, -d)
        if n+1<T and wheels[n][2]^wheels[n+1][6]:
            turn(n+1, -d)

        if d==1:
            k = wheels[n].pop()
            wheels[n].appendleft(k)
        else:
            k = wheels[n].popleft()
            wheels[n].append(k)

    T = int(input())
    wheels = make_wheels()
    N = int(input())
    for _ in range(N):
        n, d = map(int, input().split())
        turned = set()
        turn(n-1, d)

    ret = 0
    for wheel in wheels:
        if wheel[0]: ret += 1
    return ret

print(main())
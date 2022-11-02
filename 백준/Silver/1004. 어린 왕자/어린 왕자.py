import sys
input = sys.stdin.readline

def check_is_in_planet(si, sj, pi, pj, r):
    distance = ((si-pi)**2+(sj-pj)**2)**(1/2)
    return distance < r

T = int(input())
for _ in range(T):
    bi, bj, ti, tj = map(int, input().split())
    N = int(input())
    planets = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for planet in planets:
        check1 = check_is_in_planet(bi, bj, *planet)
        check2 = check_is_in_planet(ti, tj, *planet)
        cnt += (check1+check2)%2
        
    print(cnt)
from heapq import heappop, heappush

def main():
    H = [-int(input())]
    score = 0
    while True:
        maxx = -heappop(H)
        if maxx == 1: return score
        n = maxx//2
        m = n+1 if maxx%2 else n
        score += n*m
        heappush(H, -n)
        heappush(H, -m)

print(main())
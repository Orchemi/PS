def main():
    arr = [int(input()) for _ in range(7)]
    odds = []
    for a in arr:
        if a%2:
            odds.append(a)
        
    if not odds: return [-1]
    sums = sum(odds)
    minn = min(odds)
    return [sums, minn]
    
ret = main()
for r in ret:
    print(r)
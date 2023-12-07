def main():
    M, D = 2, 18
    m = int(input())
    d = int(input())

    if m > M: return 'After'
    if m < M: return 'Before'
    if d == D: return 'Special'
    return 'After' if d > D else 'Before'
        
print(main())
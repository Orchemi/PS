def main():
    N = int(input())
    if N == 0: return 1
    ret = 1
    for i in range(1, N+1):
        ret *= i
    return ret
    
print(main())
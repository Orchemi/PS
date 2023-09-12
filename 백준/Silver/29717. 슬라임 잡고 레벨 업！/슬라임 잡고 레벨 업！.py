def main():
    N = int(input())
    total_exp = N*(N+1)//2
    lv = int(total_exp**(1/2)) + 1
    while total_exp < lv*(lv-1):
        lv -= 1
    return lv


T = int(input())
for _ in range(T):
    print(main())
def main():
    txt = input()
    L = len(txt)
    P = [0]*26

    i = 0
    while i < L:
        n = ord(txt[i])-65
        P[n] += 1
        if P[n]==3:
            if i+1 >= L or txt[i+1]!=txt[i]: return 'FAKE'
            P[n] = 0
            i += 1
        i += 1
    return 'OK'


N = int(input())
for _ in range(N):
    print(main())
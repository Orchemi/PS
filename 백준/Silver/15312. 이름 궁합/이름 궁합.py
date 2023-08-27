def main():
    def find_inits():
        inits = []
        for i in range(L):
            inits.append(Hs[ord(A[i])-65])
            inits.append(Hs[ord(B[i])-65])
        return inits

    def combine():
        ret = []
        for i in range(l-1):
            n = (arr[i]+arr[i+1])%10
            ret.append(n)
        return ret


    A = input()
    B = input()
    L = len(A)
    Hs = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

    arr = find_inits()
    l = L*2
    while l > 2:
        arr = combine()
        l -= 1

    return ''.join(list(map(str, arr)))

print(main())
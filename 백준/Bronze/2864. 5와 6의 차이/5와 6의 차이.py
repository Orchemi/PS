def to_max(S):
    L = list(S)
    l = len(L)
    for i in range(l):
        if L[i] == '5':
            L[i] = '6'
    return int(''.join(L))

def to_min(S):
    L = list(S)
    l = len(L)
    for i in range(l):
        if L[i] == '6':
            L[i] = '5'
    return int(''.join(L))

a, b = input().split()
print(to_min(a)+to_min(b), to_max(a)+to_max(b))
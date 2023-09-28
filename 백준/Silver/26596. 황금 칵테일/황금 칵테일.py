def main():
    def check_golden_ratio(v1, v2):
        if v2 <= v1*1.618 < v2+1: return True
        if v1 <= v2*1.618 < v1+1: return True
        return False


    N = int(input())
    D = {}
    for _ in range(N):
        name, value = input().split()
        D[name] = D.get(name, 0) + int(value)

    keys = list(D.keys())
    kl = len(keys)
    for i in range(kl):
        val1 = D[keys[i]]
        for j in range(i+1, kl):
            val2 = D[keys[j]]
            if check_golden_ratio(val1, val2): return 'Delicious!'
    return 'Not Delicious...'

print(main())
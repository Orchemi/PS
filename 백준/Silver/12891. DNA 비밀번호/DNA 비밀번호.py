import sys
input = sys.stdin.readline

def main():
    def find_init_counts():
        init_counts = {
            'A': 0,
            'C': 0,
            'G': 0,
            'T': 0,
        }
        for i in range(P):
            if not dna[i] in D: continue
            init_counts[dna[i]] += 1
        return init_counts

    def find_is_possible(cur_counts):
        for d in D:
            if cur_counts[d] < needs[d]: return False
        return True

    S, P = map(int, input().split())
    D = set('ACGT')
    dna = input()
    [A, C, G, T] = list(map(int, input().split()))
    needs = {'A': A, 'C':C, 'G':G, 'T':T}

    ret = 0
    cur_counts = find_init_counts()
    for i in range(S-P+1):
        ret += find_is_possible(cur_counts)
        if i+P==S: break
        if dna[i] in D:
            cur_counts[dna[i]] -= 1
        if dna[i+P] in D:
            cur_counts[dna[i+P]] += 1
    return ret

print(main())
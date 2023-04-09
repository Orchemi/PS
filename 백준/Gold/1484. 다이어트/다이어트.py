def main():
    G = int(input())
    ret = []
    for n in range(1, int(G**(1/2))+1):
        if G%n: continue
        n1, n2 = n, G//n
        if not (n1 and n2): continue
        if (n1==n2) or (n1+n2)%2: continue
        ret.append((n1+n2)//2)

    return ret[::-1] if ret else [-1]

print(*main(), sep='\n')
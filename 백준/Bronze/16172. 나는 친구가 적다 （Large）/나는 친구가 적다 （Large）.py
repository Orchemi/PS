S, K = input(), input()
L = ''.join([i for i in S if not i.isdigit()])
print(0 if len(L.split(K))==1 else 1)
D = {}
keys = ['Re','Pt','Cc','Ea','Tb','Cm','Ex']
for k in keys:
    D[k] = 0

N = 0
while True:
    try:
        arr = input().split()
        for a in arr:
            N += 1
            if not a in keys: continue
            D[a] += 1
    except:
        break

for k in keys:
    print(k, D[k], f'{float(D[k] / N):.2f}')
print(f'Total {N} 1.00')
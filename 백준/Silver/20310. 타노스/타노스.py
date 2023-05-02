txt = input()
D = {'1':0, '0':0}
for t in txt:
    D[t] += 1
print('0'*(D['0']//2)+'1'*(D['1']//2))
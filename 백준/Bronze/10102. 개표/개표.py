N = int(input())
txt = input()
D = {'A':0, 'B':0}
for t in txt:
    D[t]+=1
    
a, b = D['A'], D['B']
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')
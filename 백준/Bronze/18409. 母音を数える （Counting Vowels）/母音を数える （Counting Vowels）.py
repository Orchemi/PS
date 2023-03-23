m = 'aeiou'
N = int(input())
txt = input()

ret = 0
for t in txt:
    if t in m:
        ret += 1
        
print(ret)
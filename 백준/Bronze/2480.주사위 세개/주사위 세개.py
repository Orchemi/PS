lst = list(map(int, input().split()))
cnt = [0]*7

for i in lst:
    cnt[i] += 1

if max(cnt)==3:
    print(10000+lst[0]*1000)
elif max(cnt)==2:
    for i, c in enumerate(cnt):
        if c==2:
            print(1000 + i*100)
else:
    print(max(lst)*100)
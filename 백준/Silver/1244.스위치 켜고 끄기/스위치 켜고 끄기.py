import sys
input = sys.stdin.readline

on_off = {1:0, 0:1}
n = int(input())
switch = list(map(int, input().split()))
t = int(input())
for _ in range(t):
    s, num = map(int, input().split())
    if s == 1:
        i = num
        while num-1<n:
            switch[num-1] = on_off[switch[num-1]]
            num += i
    else:
        i, j = num-2, num
        switch[num-1] = on_off[switch[num-1]]
        while i>=0 and j<n:
            if switch[i] == switch[j]:
                switch[i] = on_off[switch[i]]
                switch[j] = on_off[switch[j]]
            else:
                break
            i -= 1
            j += 1

for i in range(0, n, 20):
    print(*switch[i:i+20])
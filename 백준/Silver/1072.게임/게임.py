X, Y = map(int, input().split())
k = (Y*100)//X

if (X==Y) or (k==99):
    print(-1)
    quit()

ans = ((100*Y) - ((k+1)*X)) // (k-99)
if ((100*Y) - ((k+1)*X)) % (k-99):
    ans += 1

print(ans)
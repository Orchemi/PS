N = int(input())
arr = list(map(int, input().split()))

V = 0
for a in arr:
    new_V = 1-(1-V)*(1-a*0.01)
    print(new_V*100)
    V = new_V
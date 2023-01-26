T = int(input())
for t in range(1, T+1):
    arr = sorted(list(map(int, input().split())))
    ret = 'yes' if arr[2]**2 == arr[0]**2+arr[1]**2 else 'no'
    print(f'Scenario #{t}:')
    print(ret)
    print()
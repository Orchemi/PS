def main():
    diffs = set()
    for i in range(N-1):
        diff = abs(arr[i]-arr[i+1])
        diffs.add(diff)

    for i in range(1, N):
        if not i in diffs: return 'Not jolly'
    return 'Jolly'

while True:
    try:
        N, *arr = map(int, input().split())
        print(main())
    except:
        break
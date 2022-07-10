def main():
    N = int(input())
    std, *arr = list(map(int, input().split()))
    arr.sort()
    for a in arr:
        if std <= a: return 0
        std += a
    return 1

print('Yes' if main() else 'No')
def main():
    N = int(input())
    arr = list(map(int, input().split()))[::-1]
    stack = []

    n = 1
    while n < N and arr:
        if stack and stack[-1] == n:
            stack.pop()
            n += 1
            continue

        a = arr.pop()
        if a == n:
            n += 1
            continue

        stack.append(a)

    return 'Nice' if sorted(stack, reverse=True) == stack else 'Sad'


print(main())
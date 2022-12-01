def main():
    N = int(input())
    five = N//5
    while five >= 0:
        M = N-five*5
        if not M%2: return five+M//2
        five -= 1
    return -1

print(main())
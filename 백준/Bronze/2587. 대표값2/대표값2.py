def main():
    arr = [int(input()) for _ in range(5)]
    avg = sum(arr)//5
    mid = sorted(arr)[2]
    return avg, mid

for n in main():
    print(n)
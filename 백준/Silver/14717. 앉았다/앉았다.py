def main():
    def calc_score(n1, n2):
        if n1==n2: return n1*10
        return (n1+n2)%10

    arr = []
    for i in range(1, 11):
        arr.append(i)
        arr.append(i)

    a, b = map(int, input().split())
    for n in (a, b):
        for i in range(20):
            if arr[i] == n:
                arr.pop(i)
                break

    std = calc_score(a, b)
    all_cnt = 0
    cur_cnt = 0
    for i in range(17):
        for j in range(i+1, 18):
            all_cnt += 1
            if calc_score(arr[i], arr[j]) < std:
                cur_cnt += 1

    return f'{cur_cnt/all_cnt:.3f}'

print(main())
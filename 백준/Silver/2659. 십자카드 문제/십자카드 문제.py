def main():
    def make_num(arr):
        ret = 0
        for i in range(4):
            ret += arr[i]*(10**(3-i))
        return ret

    def find_clock_number(arr):
        nums = []
        for _ in range(4):
            n = make_num(arr)
            nums.append(n)
            h = arr.pop(0)
            arr.append(h)
        return sorted(nums)[0]

    def create_all_clock_number():
        clock_numbers = set()
        for a in range(1, 10):
            for b in range(1, 10):
                for c in range(1, 10):
                    for d in range(1, 10):
                        cur_clock_number = find_clock_number([a, b, c, d])
                        clock_numbers.add(cur_clock_number)
        return sorted(list(clock_numbers))

    def count():
        cnt = 0
        L = len(clock_numbers)
        while clock_numbers[cnt] <= std_n:
            cnt += 1
            if cnt == L: return L
        return cnt

    std_arr = list(map(int, input().split()))
    std_n = find_clock_number(std_arr)
    clock_numbers = create_all_clock_number()
    return count()

print(main())
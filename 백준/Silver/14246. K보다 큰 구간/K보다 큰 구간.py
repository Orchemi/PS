def main():
    N = int(input())
    nums = list(map(int, input().split()))
    k = int(input())

    cnt = 0
    left, right = 0, 0
    S = 0
    while right <= N:
        while S > k:
            cnt += (N-(right-1))
            S -= nums[left]
            left += 1
        else:
            if right >= N: return cnt
            S += nums[right]
            right += 1

    return cnt

print(main())
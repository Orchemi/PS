import sys
input = sys.stdin.readline

def main():
    def is_good(k):
        target = nums[k]
        s, e = 0, N-1
        while True:
            if s==k: s+=1
            if e==k: e-=1
            if s >= e: break
            cur_sum = nums[s]+nums[e]
            if cur_sum == target: return True
            if cur_sum > target:
                e-=1
            else:
                s+=1
        return False

    N = int(input())
    nums = sorted(list(map(int, input().split())))
    ret = 0
    for k in range(N):
        ret += is_good(k)
    return ret

print(main())
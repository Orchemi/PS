def main():
    def organize_arr(arr):
        fail_S = set()
        team6_S = set()
        new_arr = []
        for a in arr:
            if a in team6_S:
                new_arr.append(a)
                continue
            if a in fail_S: continue
            if arr.count(a) == 6:
                team6_S.add(a)
                new_arr.append(a)
            else:
                fail_S.add(a)
        return new_arr

    def check_score():
        D = {}
        for i in range(N):
            t = arr[i]
            if not D.get(t, []):
                D[t] = []
            D[t].append(i+1)
        return D

    def organize_applicant(D):
        ret_team_num = 1e4
        ret_member_5 = 1e4
        min_score = 1e4
        for team_num, team_members in D.items():
            score = sum(team_members[:4])
            if min_score > score:
                min_score = score
                ret_member_5 = team_members[4]
                ret_team_num = team_num

            elif min_score == score:
                if ret_member_5 < team_members[4]: continue
                ret_member_5 = team_members[4]
                ret_team_num = team_num
        return ret_team_num

    N = int(input())
    arr = list(map(int, input().split()))
    arr = organize_arr(arr)
    N = len(arr)
    D = check_score()
    return organize_applicant(D)

T = int(input())
for _ in range(T):
    print(main())
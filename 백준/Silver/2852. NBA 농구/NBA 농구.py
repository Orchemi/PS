def main():
    def record_goals():
        goals = [['0', '00:00']] + [input().split() for _ in range(N)] + [['0', '48:00']]
        for i in range(N+2):
            goals[i][0] = int(goals[i][0])
            goals[i][1] = calc_to_second(goals[i][1])
        return goals

    def calc_to_second(time):
        m, s = map(int, time.split(':'))
        return m*60+s

    def calc_to_minute(time):
        m, s = time//60, time%60
        mm = '0'*(2-len(str(m)))+f'{m}'
        ss = '0'*(2-len(str(s)))+f'{s}'
        return f'{mm}:{ss}'

    def find_win_team():
        if scores[1] > scores[2]: return 1
        if scores[2] > scores[1]: return 2
        return 0


    N = int(input())
    goals = record_goals()
    scores = [0]*3
    win_times = [0]*3

    for i in range(1, N+2):
        t, time = goals[i]
        win_team = find_win_team()
        win_times[win_team] += (time - goals[i-1][1])
        scores[t] += 1

    return calc_to_minute(win_times[1]), calc_to_minute(win_times[2])

print(*main(), sep='\n')
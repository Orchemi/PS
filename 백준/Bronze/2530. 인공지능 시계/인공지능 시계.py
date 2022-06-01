H, M, S = map(int, input().split())
timedelta = int(input())
time_total = (H*3600+M*60+S) + timedelta

time_total = time_total % (24*60*60)
H2, M2S2 = time_total // (60*60), time_total % (60*60)
M2, S2 = M2S2 // 60, M2S2 % 60

print(H2, M2, S2)
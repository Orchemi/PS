H, M = map(int, input().split())

time_val = H * 60 + M


if time_val < 45:
    time_val += (24 * 60)

H1 = (time_val - 45) // 60
M1 = (time_val - 45) % 60

print(f'{H1} {M1}')

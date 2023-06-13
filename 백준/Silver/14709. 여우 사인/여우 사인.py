def main():
    pos = {(1,3),(3,1),(1,4),(4,1),(3,4),(4,3)}
    tar = {(1,3),(1,4),(3,4)}
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        if not (a, b) in pos: return False
        tar = tar - {(a, b)} - {(b, a)}

    if tar: return False
    return True

print('Wa-pa-pa-pa-pa-pa-pow!' if main() else 'Woof-meow-tweet-squeek')
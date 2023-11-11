import sys
input = sys.stdin.read

def main():
    def consider_word_part(t):
        if t == '-': return True
        if 'a' <= t <= 'z': return True
        if 'A' <= t <= 'Z': return True
        return False

    txt = input()
    longest = ''
    longest_l = 0
    cur_word = ''
    cur_l = 0
    for t in txt:
        if consider_word_part(t):
            cur_word += t
            cur_l += 1
        else:
            if cur_l > longest_l:
                longest = cur_word
                longest_l = cur_l
            cur_word = ''
            cur_l = 0

    return longest.lower()

print(main())
import sys

def is_group_word(word):
    char_list = []
    for c in word:
        if c not in char_list:
            char_list.append(c)
        elif c != char_list[-1]:
            return False
    return True

N = int(sys.stdin.readline().strip())
count = 0
for _ in range(N):
    word = sys.stdin.readline().strip()
    if is_group_word(word):
        count += 1

print(count)
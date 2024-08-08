from collections import Counter

word = input().strip()

word = word.upper()

freq = Counter(word)

max_freq = max(freq.values())

most_common_chars = [char for char, count in freq.items() if count == max_freq]

if len(most_common_chars) > 1:
    print('?')
else:
    print(most_common_chars[0])

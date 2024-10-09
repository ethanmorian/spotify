from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for char in ransom_counter:
            if ransom_counter[char] > magazine_counter.get(char, 0):
                return False

        return True

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = {}
        
        for i, char in enumerate(s):
            hash_table[char] = hash_table.get(char, 0) + 1

        for i in range(len(s)):
            if hash_table[s[i]] == 1:
                return i
                
        return -1
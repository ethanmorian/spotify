class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h = {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i, j in zip(pattern, words):
            if i in h:
                if h[i] != j:
                    return False
            else:
                h[i] = j

        return True
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}

        for i, v in enumerate(nums):
            if v in h and i - h[v] <= k:
                return True
            h[v] = i

        return False
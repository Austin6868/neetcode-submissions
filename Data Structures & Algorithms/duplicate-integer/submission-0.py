from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_map = defaultdict(int)
        for num in nums:
            dup_map[num] += 1
            if dup_map[num] > 1:
                return True
        return False
            
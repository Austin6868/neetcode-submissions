class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        upper = 0
        lower = 0
        num_set = set()
        curr = 1
        res = 0
        for num in nums:
            upper = max(num, upper)
            lower = min(num, lower)
            num_set.add(num)

        for i in range(lower, upper + 1):
            if i - 1 in num_set and i in num_set:
                curr += 1
            else:
                res = max(curr, res)
                curr = 1
        res = max(curr, res)
        return res

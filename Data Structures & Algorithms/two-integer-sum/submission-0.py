class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        gap_dict = {}
        for i in range(len(nums)):
            gap = target - nums[i]
            if gap in gap_dict:
                return [gap_dict[gap] ,i]
            else:
                gap_dict[nums[i]] = i

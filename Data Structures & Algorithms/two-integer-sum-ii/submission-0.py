class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            c_l = numbers[l]
            c_r = numbers[r]
            if c_r + c_l < target:
                l += 1
            elif c_r + c_l > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return [l, r]
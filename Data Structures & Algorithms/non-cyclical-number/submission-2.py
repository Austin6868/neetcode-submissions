class Solution:
    def sumAll(self, n: int) -> int:
        sum_all = 0
        while n:
            temp = n % 10
            sum_all += temp ** 2
            n = n//10
        return sum_all

    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = n
        while curr not in seen:
            seen.add(curr)
            curr = self.sumAll(curr)
            if curr == 1:
                return True
        return False

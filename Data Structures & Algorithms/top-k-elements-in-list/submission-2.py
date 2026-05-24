from heapq import heappush, heappop, heapify
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        freq_heap = []
        result = []
        for num in nums:
            freq_dict[num] += 1
        print(freq_dict)
        for key in freq_dict.keys():
            heappush(freq_heap, (-freq_dict[key], key))
        for i in range(k):
            result.append(heappop(freq_heap)[1])
        return result
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup_map = defaultdict(list)
        result = []
        for string in strs:
            lookup_map[self.generateMap(string)].append(string)
        for value in lookup_map.values():
            result.append(value)
        return result
        
    def generateMap(self, string: str):
        result_map = [0] * 26
        for char in string:
            result_map[ord(char) - ord('a')] += 1
        return tuple(result_map)
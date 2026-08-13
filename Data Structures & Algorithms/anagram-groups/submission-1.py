class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        di = defaultdict(list)
        
        for s in strs:
            count = [0]*26
            for l in s:
                count[ord(l) - ord('a')] += 1
            di[tuple(count)].append(s)
        return list(di.values())

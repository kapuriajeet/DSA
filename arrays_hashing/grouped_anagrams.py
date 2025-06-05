from collections import defaultdict

strs = ["act","pots","tops","cat","stop","hat", "fool"]
class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
            print("Res -- ", res)
        return res.values()

solution = Solution()
print(solution.groupAnagrams(strs))
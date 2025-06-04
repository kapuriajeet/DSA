strs = ["bat","bag","bank","band"]

# TC - O (n * m)
# SC - O(1)
class Solution:
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]  

soluton = Solution()
print(soluton.longestCommonPrefix(strs))
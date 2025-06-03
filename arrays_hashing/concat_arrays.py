# Leetcode 1929.
# Concat two arrays


# First Solution 
# TC - O(n)
# SC - O(n)
class SolutionOne:
    def getConcatenation(self, nums):
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans

# Second solution
# TC - O(n)
# SC - O(n)
class SolutionTwo:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)
        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num
        return ans

# Simple Python way
class SolutionThree:
    def getConcatenation(self, nums):
        return nums + nums



nums = [1,2,1]
solOne = SolutionOne()
solTwo = SolutionTwo()
solThree = SolutionThree()


print(solOne.getConcatenation(nums))
print(solTwo.getConcatenation(nums))
print(solThree.getConcatenation(nums))
        
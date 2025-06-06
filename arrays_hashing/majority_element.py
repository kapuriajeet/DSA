from collections import defaultdict


nums = [3, 3, 4]

# Brute Force
# TC - O(n ** 2)
# SC - O(1)

class BfSolution():
    def majorityElement(self, nums):
        n = len(nums)
        for num in nums:
            count = sum(1 for i in nums if i == num)
            if count > n // 2:
                return num

bfSolution = BfSolution()
# print(bfSolution.majorityElement(nums))

# Hashmap solution
# TC - O(n)
# SC - O(n)
class Solution:
    def majorityElement(self, nums):
        count = defaultdict(int)
        res = maxCount = 0
        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res


solution = Solution()
print(solution.majorityElement(nums))
             
# Optimal
# TC - O(n)
# SC - O(1)
class OSolution():
    def majorityElement(self, nums):
        res = count = 0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if res == num else -1)
        return res
    
optimalSolution = OSolution()
print(optimalSolution.majorityElement(nums))

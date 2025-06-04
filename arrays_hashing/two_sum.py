nums = [3,4,5,6]
target = 7

# First Solution
# TC - O(n ** 2)
# SC - O(1)

class SolutionOne:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
solutionOne = SolutionOne()
print(solutionOne.twoSum(nums, target))


# Second Solution
class SolutionTwo:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

solutionTwo = SolutionTwo()
print(solutionTwo.twoSum(nums, target))
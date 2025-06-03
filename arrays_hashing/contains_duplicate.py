# First Solution
nums = [1, 2, 3, 3]

# Brute Force
# TC - O(n ** 2)
# SC - O(1)

class SolutionOne:
    def hasDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(nums[i] == nums[j]):
                    return True
        return False


# Second Solution
# TC - O(n)
# SC - O(n)

class SolutionTwo:
    def hasDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Third Solution
# TC - O(n)
# SC - O(n)
class SolutionThree:
    def hasDuplicate(self, nums):
        return (len(nums) > len(set(nums)))



solOne = SolutionOne()
solTwo = SolutionTwo()
solThree = SolutionThree()
print(solOne.hasDuplicate(nums))
print(solTwo.hasDuplicate(nums))
print(solThree.hasDuplicate(nums))
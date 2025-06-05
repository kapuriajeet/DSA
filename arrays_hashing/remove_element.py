nums = [0,1,2,2,3,0,4,2]
val = 2
# First Solution
# TC - O(n)
# SC - O(n)

class Solution:
    def removeElement(self, nums, val):
        temp = []
        for num in nums:
            if num == val:
                continue
            temp.append(num)
        return len(temp)
        
solution = Solution()
print(solution.removeElement(nums, val))


# Second solution - Two Pointer
# TC - O(n)
# SC - O(1)
class SolutionTwo:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

solutionTwo = SolutionTwo()
print(solutionTwo.removeElement(nums, val))
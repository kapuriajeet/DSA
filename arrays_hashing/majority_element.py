nums = [3, 3, 4]
class Solution:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        print(count)
        for i in count:
            print(i)
            print(count[i])
            if count[i] > len(nums) / 2:
                ans = i
        return ans

solution = Solution()
print(solution.majorityElement(nums))
             
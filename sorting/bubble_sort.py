nums = [5, 4, 1, 3, 9, 10, 5, 4, 2, 0]
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

print(bubble_sort(nums))
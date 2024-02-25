class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif not nums:
            return 0
        else:
            for i, n in enumerate(nums):
                if n > target:
                    return i
            return i + 1
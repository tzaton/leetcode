class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ln = len(nums)

        for n in set(nums):
            if nums.count(n) > ln / 2:
                return n
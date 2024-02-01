class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        i = 0

        for n in list(nums):
            if n in unique:
                del nums[i]
            else:
                unique.add(n)
                i += 1
        
        return len(nums)
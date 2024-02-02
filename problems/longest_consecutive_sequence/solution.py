class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        sequence = 0
        max_sequence = 0

        for i, n in enumerate(nums):
            if i == 0:
                sequence = 1
                continue

            if nums[i - 1] == n - 1:
                sequence += 1
            else:
                if sequence > max_sequence:
                    max_sequence = sequence
                sequence = 1
        
        return max(sequence, max_sequence)
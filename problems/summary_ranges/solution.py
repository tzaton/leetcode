class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        for i, n in enumerate(nums):
            if i == 0:
                summary = [[n]]
                continue

            if n == nums[i-1] + 1:
                summary[-1].append(n)
            else:
                summary.append([n])
        
        return [str(a[0]) if len(a) == 1 else f"{a[0]}->{a[-1]}" for a in summary]
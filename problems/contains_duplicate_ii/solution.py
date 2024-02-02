from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        for val, cnt in count.items():
            if cnt >= 2:
                idxs = [i for i, e in enumerate(nums) if e == val]
                for i, a in enumerate(idxs):
                    for j, b in enumerate(idxs):
                        if i != j and abs(a-b) <= k:
                            return True


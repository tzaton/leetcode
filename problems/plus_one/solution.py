class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join(str(d) for d in digits)
        new_num = int(num) + 1

        return [int(d) for d in list(str(new_num))]
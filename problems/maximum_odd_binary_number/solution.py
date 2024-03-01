class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ss = sorted(s, reverse=True)
        one = ss.pop(0)
        return "".join(ss) + one
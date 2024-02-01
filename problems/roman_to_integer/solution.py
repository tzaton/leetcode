class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        out = 0

        for i, num in enumerate(s):
            if i < len(s) - 1 and (
                (num == "I" and s[i + 1] in ("V", "X"))
                or (num == "X" and s[i + 1] in ("L", "C"))
                or (num == "C" and s[i + 1] in ("D", "M"))
            ):
                out -= mapping[num]
            else:
                out += mapping[num]
    
        return out
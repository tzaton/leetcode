class Solution:
    def isHappy(self, n: int) -> bool:       
        seen = []
        while True:
            n = sum(int(x)**2 for x in list(str(n)))

            if n in seen:
                return False

            if n == 1:
                return True

            seen.append(n)

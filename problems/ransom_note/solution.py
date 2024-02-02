class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for r in ransomNote:
            if magazine == magazine.replace(r, "", 1):
                return False
            magazine = magazine.replace(r, "", 1)
        return True

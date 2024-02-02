class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = dict(zip(pattern, s.split()))

        return len(set(mapping.values())) == len(mapping.values()) and " ".join(mapping.get(x, "") for x in pattern) == s
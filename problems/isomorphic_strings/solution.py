class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict(zip(s, t))
        return len(set(mapping.values())) == len(mapping.values()) and "".join(mapping[x] for x in s) == t
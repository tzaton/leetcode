class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        
        for anagram, string in (("".join(sorted(s)), s) for s in strs):
            if anagram in output:
                output[anagram].append(string)
            else:
                output[anagram] = [string]
        
        return list(output.values())
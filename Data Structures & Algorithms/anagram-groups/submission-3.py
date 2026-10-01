class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for _str in strs:
            key = "".join(sorted(_str))
            anagrams.setdefault(key, [])
            anagrams[key].append(_str)
            
        return list(anagrams.values())
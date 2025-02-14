class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        hm=defaultdict(list)
        for word in strs:
            sword=tuple(sorted(word))
            hm[sword].append(word)
        return list(hm.values())
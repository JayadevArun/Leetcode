class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1)!=set(word2):
            return False
        c1=Counter(word1)
        c2=Counter(word2)
        return sorted(c1.values())==sorted(c2.values())
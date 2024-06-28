class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        word=strs[0]
        for i in range(len(word)):
            for s in strs[1:]:
                if i==len(s) or word[i]!=s[i]:
                    return word[:i]
        return word
        

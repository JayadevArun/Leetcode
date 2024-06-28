class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        word=strs[0]
        for i in range(len(word)):
            for s in strs:
                if i==len(s) or word[i]!=s[i]:
                    return result
            result+=word[i]
        return result
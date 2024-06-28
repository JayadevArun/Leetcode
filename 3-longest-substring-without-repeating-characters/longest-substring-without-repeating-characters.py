class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=set()
        l=0
        result=0
        for ss in s:
            while ss in chars:
                chars.remove(s[l])
                l+=1
            chars.add(ss)
            if len(chars)>result:
                result=len(chars)
        return result
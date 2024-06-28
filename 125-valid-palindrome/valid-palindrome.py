class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for letter in s:
            if(letter.isalnum()):
                l.append(letter.lower())
        return l==l[::-1]
        
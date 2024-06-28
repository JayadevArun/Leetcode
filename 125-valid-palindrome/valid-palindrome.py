class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        s=s.lower()
        while(left<=right):
            if s[left].isalnum() and s[right].isalnum() and s[left]==s[right]:
                left=left+1
                right=right-1
            elif s[left].isalnum() and s[right].isalnum():
                return False
            elif s[left].isalnum():
                right=right-1
            elif s[right].isalnum():
                left=left+1
            else:
                left=left+1
                right=right-1
        return True
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s=="":
            return 0

        l=0
        r=0
        m=0

        for i in s:
            if i=='(':
                l+=1
            else:
                r+=1
            if l==r:
                m=max(m,2*l)
            elif r>l:
                l=0
                r=0

        l=0
        r=0

        for i in reversed(s):
            if i=='(':
                l+=1
            else:
                r+=1
            if l==r:
                m=max(m,2*l)
            elif l>r:
                l=0
                r=0

        return m
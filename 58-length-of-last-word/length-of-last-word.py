class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t=s.strip()
        r=t[::-1]
        c=0
        for i in range(len(r)):
            if i==len(r)-1:
                return len(r)
            if r[i]!=" ":
                c+=1
            else:
                return c
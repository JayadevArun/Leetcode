class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels=['a','e','i','o','u','A','E','I','O','U']
        c=0
        m=0

        for i in range(k):
            if s[i] in vowels:
                c+=1
                
        m=c

        for i in range(k,len(s)):
            if s[i] in vowels:
                c+=1
            if s[i-k] in vowels:
                c-=1
            m=max(m,c)
        
        return m
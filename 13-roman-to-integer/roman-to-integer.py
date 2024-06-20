class Solution:
    def romanToInt(self, s: str) -> int:
        integer=0

        hm={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000  
        }

        l=len(s)
        for i in range(l):
            if  i<l-1 and hm[s[i]]<hm[s[i+1]]:
                integer-=hm[s[i]]
            else:
                integer+=hm[s[i]]
        
        return integer
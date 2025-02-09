class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        hm1={}
        hm2={}

        for ch in t:
            hm1[ch]=1+hm1.get(ch,0)

        have=0
        need=len(hm1)
        res=[-1,-1]
        resl=float("inf")

        l=0
        for r in range(len(s)):
            ch=s[r]
            hm2[ch]=1+hm2.get(ch,0)

            if ch in hm1 and hm2[ch]==hm1[ch]:
                have+=1
            
            while have==need:
                if r-l+1<resl:
                    res=[l,r]
                    resl=r-l+1
                
                hm2[s[l]]=hm2.get(s[l],0)-1
                if s[l] in hm1 and hm2[s[l]]<hm1[s[l]]:
                    have-=1
                
                l+=1

        [left,right]=res
        if resl==float("inf"):
            return ""
        else:
            return s[left:right+1]

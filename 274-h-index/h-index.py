class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        h=0
        for i in range(1,n+1):
            count=0
            for c in citations:
                if c>=i:
                    count+=1
            if count>=i:
                h=i
        return h

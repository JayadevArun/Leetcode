class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hm={}
        L=[]
        for i in range(len(heights)):
            if heights[i] not in hm:
                hm[heights[i]]=names[i]
        l=list(hm.keys())
        l.sort(reverse=True)
        for height in l:
            L.append(hm[height])
        return L

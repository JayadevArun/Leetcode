class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm={}
        for num in arr:
            if num not in hm:
                hm[num]=1
            else:
                hm[num]+=1
        k=list(set(hm.values()))
        return len(k) == len(hm)
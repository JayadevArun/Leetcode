class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm={}
        for num in arr:
            if num not in hm:
                hm[num]=1
            else:
                hm[num]+=1
        s=set()
        for number in hm.values():
            if number in s:
                return False
            s.add(number)
        return True
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm={}
        for num in arr:
            if num not in hm:
                hm[num]=1
            else:
                hm[num]+=1
        count_list = list(hm.values())
        return len(count_list) == len(set(count_list))
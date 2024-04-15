class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        arr1 = []
        arr2 = []
        for path in paths:
            arr1.append(path[0])
            arr2.append(path[1])
        for item in arr2:
            if item not in arr1:
                return item
        
        # hm1={}
        # hm2={}
        # for path in paths:
        #     hm1[path[0]]=path[1]
        #     hm2[path[1]]=1
        # for item in hm2.keys():
        #     if item not in hm1:
        #         return item

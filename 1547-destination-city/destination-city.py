class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hm={}
        for path in paths:
            hm[path[0]]=path[1]
        for path in paths:
            if path[1] not in hm:
                return path[1]
        
        # hm1={}
        # hm2={}
        # for path in paths:
        #     hm1[path[0]]=path[1]
        #     hm2[path[1]]=1
        # for item in hm2.keys():
        #     if item not in hm1:
        #         return item
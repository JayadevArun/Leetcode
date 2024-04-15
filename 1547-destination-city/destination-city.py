class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        hm={}
        for path in paths:
            hm[path[0]]=path[1]
        for path in paths:
            if path[1] not in hm:
                return path[1]

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        if not matchsticks:
            return False
        
        tot_len=sum(matchsticks)
        if tot_len%4!=0:
            return False

        side_len=tot_len//4
        side=[0]*4
        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i==len(matchsticks):
                return True

            for j in range(4):
                if side[j]+matchsticks[i]<=side_len:
                    side[j]+=matchsticks[i]

                    if backtrack(i+1):
                        return True
                    
                    side[j]-=matchsticks[i] 
            return False

        return backtrack(0)
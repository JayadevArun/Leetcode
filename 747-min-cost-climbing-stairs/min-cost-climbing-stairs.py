class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==0:
            return 0
        if len(cost)==1:
            return cost[0]
        a=cost[0]
        b=cost[1]
        for i in range(2,len(cost)):
            temp=min(a+cost[i],b+cost[i])
            a=b
            b=temp
        return min(a,b)
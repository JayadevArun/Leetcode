class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a=cost[0]
        b=cost[1]
        for i in range(2,len(cost)):
            temp=min(a+cost[i],b+cost[i])
            a=b
            b=temp
        return min(a,b)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        dif=0
        s=0
        for i in range(len(gas)):
            dif+=gas[i]-cost[i]
            if dif<0:
                dif=0
                s=i+1
        if sum(gas)<sum(cost):
            return -1
        return s

                

        
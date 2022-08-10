class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start, fuel = 0,0
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                start, fuel = i+1, 0
        return start
    

    
    
    
    
    
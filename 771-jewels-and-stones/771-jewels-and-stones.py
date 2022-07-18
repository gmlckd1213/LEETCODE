class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        je=list(jewels)
        sum = 0
        for s in je:
            sum += stones.count(s)
        return sum
        
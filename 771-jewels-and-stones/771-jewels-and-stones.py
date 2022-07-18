class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a=list(jewels)
        su = 0
        for s in a:
            su += stones.count(s)
        return su
        
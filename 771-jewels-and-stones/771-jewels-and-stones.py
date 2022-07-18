class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a=list(jewels)
        su = 0
        for s in a:
            n=stones.count(s)
            su += n
        return su
        
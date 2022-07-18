class Solution:
    # def numJewelsInStones(self, jewels: str, stones: str) -> int:
    #     je=list(jewels)
    #     sum = 0
    #     for s in je:
    #         sum += stones.count(s)
    #     return sum
      def numJewelsInStones(self, jewels: str, stones: str) -> int:
            freqs = collections.Counter(stones)
            count = 0
            for char in jewels:
                count += freqs[char]
            return count
        
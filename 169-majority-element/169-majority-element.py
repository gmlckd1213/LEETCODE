class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        if counts.most_common(1)[0][1] > len(nums)//2:
            return counts.most_common(1)[0][0]
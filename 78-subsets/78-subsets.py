class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)+1):
            result+=list(combinations(nums,i))
        return result
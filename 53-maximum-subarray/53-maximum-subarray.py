# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         dp = [0]*len(nums)
#         dp[0] = nums[0]
#         for i in range(1, len(nums)):
#             dp[i] = max(dp[i-1]+nums[i], nums[i])
#         return max(dp)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr = 0

        for i in nums:
            if curr < 0:
                curr = 0

            curr += i

            max_sum = max(curr, max_sum)

        return max_sum
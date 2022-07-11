# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1        
        right = n + 1        
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:            
                left = mid + 1
        
        return left
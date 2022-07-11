class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            if i.isalnum():
                l.append(i.lower())
               
        # while len(l) > 1:
        #     if l.pop(0) != l.pop():
        #         return False
        # return True
        j=l.copy()
        j.reverse()
        if l == j:
            return True
        else:
            return False

        
        

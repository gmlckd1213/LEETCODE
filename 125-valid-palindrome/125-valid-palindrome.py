class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            if i.isalnum()==True:
                l.append(i.lower())
        j=l.copy()
        j.reverse()
        if l == j:
            return True
        else:
            return False
        

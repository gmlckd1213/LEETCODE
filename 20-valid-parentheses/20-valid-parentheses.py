class Solution(object):
    def isValid(self, s):
        dic = {
        ')' : '(',
        '}' : '{',
        ']' : '['
        }
        stack = []
        
        for i in s:
            if i not in dic:
                stack.append(i)
            elif (not stack) or dic[i] != stack.pop():
                return False
        return not stack
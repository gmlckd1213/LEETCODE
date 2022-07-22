class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dial = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'],'7':['p','q','r','s'], '8':['t','u','v'],'9':['w','x','y','z']}
        if len(digits) == 0:
            return
        elif len(digits) ==1:
            return dial[digits]
        else:
            result = []
            for i in digits:
                result.append(dial[i])
            if len(result)==2:
                a=product(result[0],result[1])
            elif len(result)==3:
                a=product(result[0],result[1],result[2])
            elif len(result)==4:
                a=product(result[0],result[1],result[2],result[3])
            t=[]
            for i in a:
                t.append("".join(i))
        return t
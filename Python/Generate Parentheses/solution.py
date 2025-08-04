class Solution:  
    def generateParenthesis(self, n: int):
        stack=[]
        res=[]

        def backtrack(openN,closeN):
            if openN==closeN==n:
                res.append("".join(stack))
                return
            
            if openN<n:
                stack.append("(")
                backtrack(openN+1,closeN)
                stack.pop()
            
            if closeN<openN:
                stack.append(")")
                backtrack(openN,closeN+1)
                stack.pop()
        
        backtrack(0,0)
        return res

    def generateParenthesis_dynamic(self, n):
        res = [[] for _ in range(n+1)]
        res[0] = [""]
        
        for k in range(n + 1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k-i-1]:
                        res[k].append("(" + left + ")" + right)
        
        return res[-1]
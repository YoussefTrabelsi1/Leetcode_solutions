class Solution:

    def encode(self, strs):
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        
        return res

    def decode(self, s):    
        res=[]

        for i in range(len(s)-1):
            if s[i] in [str(k) for k in range(10)] and s[i+1]=="#":
                res.append(s[i+2:i+2+int(s[i])])
        
        return res



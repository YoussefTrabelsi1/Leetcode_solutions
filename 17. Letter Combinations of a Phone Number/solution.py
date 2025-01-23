def letterCombinations(digits):
    phone={
        "2":"abc", "3":"def",
        "4":"ghi", "5":"jkl","6":"mno",
        "7":"pqrs", "8":"tuv","9":"wxyz"
    }

    if len(digits)==0:
        return []
    if len(digits)==1:
        return list(phone[digits])
    
    else:
        res=[]
        res1=letterCombinations(digits[:len(digits)-1])
        for c in phone[digits[-1]]:
            for elt in res1:
                res.append(elt+c)
            
                
        return res

digits = "23"

print(letterCombinations(digits))
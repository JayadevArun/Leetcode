class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        res=[]
        hm={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def recback(i,cur):

            if len(cur)==len(digits):
                res.append("".join(cur))
                return

            for ch in hm[digits[i]]:
                cur.append(ch)
                recback(i+1,cur)
                cur.pop()
        
        recback(0,[])
        return res

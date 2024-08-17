class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []

        def recback(low,cur,rem,k):

            if len(cur)==k and rem==0:
                res.append(cur[:])
                return

            if len(cur)>k or rem<0:
                return

            for i in range(low,10):
                cur.append(i)
                recback(i+1,cur,rem-i,k)
                cur.pop()

        recback(1,[],n,k)
        return res

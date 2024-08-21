class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        st=[]
        res=[0]*n
        for i in range(n):
            while st and temperatures[i]>temperatures[st[-1]]:
                ind=st.pop()
                res[ind]=i-ind
            st.append(i)
        return res
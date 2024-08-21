class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while st and temperatures[i]>temperatures[st[-1]]:
                ind=st.pop()
                res[ind]=i-ind
            st.append(i)
        return res
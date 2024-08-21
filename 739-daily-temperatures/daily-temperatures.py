class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        res=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while st and temp>temperatures[st[-1]]:
                ind=st.pop()
                res[ind]=i-ind
            st.append(i)
        return res
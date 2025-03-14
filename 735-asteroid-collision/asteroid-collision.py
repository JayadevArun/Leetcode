class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for ast in asteroids:
            while st and ast<0<st[-1]:
                dif=ast+st[-1]
                if dif>0:
                    ast=0
                elif dif<0:
                    st.pop()
                else:
                    ast=0
                    st.pop()
            if ast:
                st.append(ast)
        return st

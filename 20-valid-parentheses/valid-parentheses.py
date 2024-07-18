class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for item in s:
            if st:
                if item==')' and st[-1]=='(':
                    st.pop()
                elif item=='}' and st[-1]=='{':
                    st.pop()
                elif item==']' and st[-1]=='[':
                    st.pop()
                else:
                    st.append(item)
            else:
                st.append(item)
        return not st
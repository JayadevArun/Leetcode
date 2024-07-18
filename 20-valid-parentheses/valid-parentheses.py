class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for item in s:
            if item in ['(','{','[']:
                st.append(item)
            elif item==')':
                if len(st)==0:
                    return False
                if st[-1]=='(':
                    st.pop()
                else:
                    return False
            elif item=='}':
                if len(st)==0:
                    return False
                if st[-1]=='{':
                    st.pop()
                else:
                    return False
            elif item==']':
                if len(st)==0:
                    return False
                if st[-1]=='[':
                    st.pop()
                else:
                    return False
        return len(st)==0

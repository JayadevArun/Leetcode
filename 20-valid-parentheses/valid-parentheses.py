class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for item in s:
            if item in '({[':
                st.append(item)
            else:
                if not st:
                    return False
                top=st.pop()
                if item==')' and top!='(':
                    return False
                if item=='}' and top!='{':
                    return False
                if item==']' and top!='[':
                    return False
        return not st
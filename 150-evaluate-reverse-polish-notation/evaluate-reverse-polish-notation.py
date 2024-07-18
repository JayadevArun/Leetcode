class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for item in tokens:
            if item=='+':
                st.append(st.pop()+st.pop())
            elif item=='-':
                a=st.pop()
                b=st.pop()
                st.append(b-a)
            elif item=='*':
                st.append(st.pop()*st.pop())
            elif item=='/':
                c=st.pop()
                d=st.pop()
                st.append(int(d/c))
            else:
                st.append(int(item))
        return st[0]
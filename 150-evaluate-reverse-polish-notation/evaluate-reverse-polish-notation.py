class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for item in tokens:
            if item in "+-*/":
                b = st.pop()
                a = st.pop()
                if item == '+':
                    st.append(a + b)
                elif item == '-':
                    st.append(a - b)
                elif item == '*':
                    st.append(a * b)
                elif item == '/':
                    st.append(int(a / b))
            else:
                st.append(int(item))
        return st[0]
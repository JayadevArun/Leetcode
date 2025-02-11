class Solution:
    def calculate(self, s: str) -> int:

        st=[]
        num=0
        sign=1
        res=0

        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)

            elif ch in "+-":
                res+=sign*num
                num=0
                sign=1 if ch=="+" else -1

            elif ch=="(":
                st.append(res)
                st.append(sign)
                res=0
                sign=1

            elif ch==")":
                res+=sign*num
                res*=st.pop()
                res+=st.pop()
                num=0

        return res+sign*num
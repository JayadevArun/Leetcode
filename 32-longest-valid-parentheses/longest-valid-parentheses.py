class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if s=="":
            return 0

        st=[-1]
        c=0

        for i in range(len(s)):
            if s[i]=="(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    c=max(c,i-st[-1])

        return c

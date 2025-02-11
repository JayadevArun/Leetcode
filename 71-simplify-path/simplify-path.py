class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        pa=path.split("/")
        for p in pa:
            if p=="..":
                if st:
                    st.pop()
            elif p and p!=".":
                    st.append(p)
        return "/"+"/".join(st)
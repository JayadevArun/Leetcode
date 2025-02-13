class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        pa=path.split("/")
        for p in pa:
            if p=="..":
                if st:
                    st.pop()
            else:
                if p:
                    if p!=".":
                        st.append(p)
        return "/"+"/".join(st)
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s[::-1]
        s=s.split(" ")
        s=s[::-1]
        return " ".join(s)

        # res=""
        # words=s.split()
        # for word in words:
        #     rev=word[::-1]
        #     res+=rev
        #     res+=" "
        # return res.rstrip()

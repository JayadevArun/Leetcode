class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res=""
        c=0

        a=a[::-1]
        b=b[::-1]

        for i in range(max(len(a),len(b))):

            d1 = ord(a[i]) - ord("0") if i < len(a) else 0
            d2 = ord(b[i]) - ord("0") if i < len(b) else 0

            tot=d1+d2+c
            ch=str(tot%2)
            res=ch+res
            c=tot//2

        if c:
            res="1"+res
        return res
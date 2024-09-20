class Solution:
    def intToRoman(self, num: int) -> str:
        hp=[
            ("M",1000),
            ("CM",900),
            ("D",500),
            ("CD",400),
            ("C",100),
            ("XC",90),
            ("L",50),
            ("XL",40),
            ("X",10),
            ("IX",9),
            ("V",5),
            ("IV",4),
            ("I",1)
        ]
        res=[]
        for s,v in hp:
            c=num//v
            if c:
                res.append(s*c)
                num-=v*c
        return ''.join(res) 
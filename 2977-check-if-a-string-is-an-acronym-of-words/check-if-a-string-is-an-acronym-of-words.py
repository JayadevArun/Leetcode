class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        l=[]
        for i in words:
            l.append(i[0])
        if "".join(l)==s:
            return True

        # if len(words)!=len(s):
        #     return False
        # for i in range(len(words)):
        #     if words[i][0] != s[i]:
        #         return False
        # return True 
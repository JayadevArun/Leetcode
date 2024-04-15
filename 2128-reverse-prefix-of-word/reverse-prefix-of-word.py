class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l=[]
        f=False
        for letter in word:
            if letter!=ch and f==False:
                l.append(letter)
            if letter!=ch and f==True:
                l.append(letter)
            if letter==ch and f==True:
                l.append(letter)
            if letter==ch and f==False:
                l.append(letter)
                l.reverse()
                f=True
        res="".join(l)
        return res
        

        


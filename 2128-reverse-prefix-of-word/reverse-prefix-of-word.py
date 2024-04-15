class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index=0
        for i in range(len(word)):
            if word[index]==ch:
                return word[index::-1]+word[index+1:]
            index+=1
        return word

        # l=[]
        # f=False
        # for letter in word:
        #     if letter!=ch and f==False:
        #         l.append(letter)
        #     if letter!=ch and f==True:
        #         l.append(letter)
        #     if letter==ch and f==True:
        #         l.append(letter)
        #     if letter==ch and f==False:
        #         l.append(letter)
        #         l.reverse()
        #         f=True
        # res="".join(l)
        # return res
        

        


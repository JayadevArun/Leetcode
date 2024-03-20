class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=[]
        for i,item in enumerate(words):
            if x in item:
                l.append(i)
        return l


        # l=[]
        # for i in range(len(words)):
        #     if x in words[i]:
        #         l.append(i)
        # return l